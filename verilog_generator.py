from fsm import FSM
from math import floor, log
from abc import abstractmethod


class VerilogComponentGenerator:
    def __init__(self, indent_lvl):
        self.indent_lvl = indent_lvl

    def add_indent(self, code):
        code_splitted = code.split("\n")
        for i in range(len(code_splitted)):
            code_splitted[i] = " " * self.indent_lvl + code_splitted[i]
        return "\n".join(code_splitted) + "\n"

    @abstractmethod
    def generate_code(self):
        pass


class VerilogAlwaysGenerator(VerilogComponentGenerator):
    @staticmethod
    def __converts_ports_to_code(ports):
        return ", ".join(ports)

    def generate_code(self, ports, body_code):
        result_code = ""
        result_code += f"always@({self.__converts_ports_to_code(ports)}) begin\n\n"
        result_code += self.add_indent(body_code)
        result_code += "end\n\n"
        return result_code


class VerilogInitialGenerator(VerilogComponentGenerator):
    @staticmethod
    def __converts_ports_to_code(ports):
        return ", ".join(ports)

    def generate_code(self, body_code):
        result_code = ""
        result_code += f"initial begin\n"
        result_code += self.add_indent(body_code)
        result_code += "end\n\n"
        return result_code


class VerilogCaseItemGenerator(VerilogComponentGenerator):
    def generate_code(self, case_item_value, case_item_body):
        result_code = ""
        result_code += f"{case_item_value}: begin\n"
        result_code += self.add_indent(case_item_body)
        result_code += "end\n"
        return result_code


class VerilogCaseGenerator(VerilogComponentGenerator):
    @staticmethod
    def __converts_ports_to_code(ports):
        return ", ".join(ports)

    def generate_code(self, ports, case_items):
        result_code = ""
        result_code += f"case({self.__converts_ports_to_code(ports)})\n"
        for item in case_items:
            result_code += self.add_indent(item)
        result_code += "endcase\n"
        return result_code


class VerilogFSMGenerator:
    EMPTY = ""

    def __init__(self, fsm: FSM):
        self.__verilog_code = self.EMPTY
        self.fsm = fsm
        self.__always_generator = VerilogAlwaysGenerator(indent_lvl=2)
        self.__case_generator = VerilogCaseGenerator(indent_lvl=2)
        self.__case_item_generator = VerilogCaseItemGenerator(indent_lvl=2)

    def __calculate_required_bits_for_states(self):
        fsm_states = self.fsm.get_states()
        required_bits_cnt = floor(log(len(fsm_states), 2)) + 1
        return required_bits_cnt

    def __get_binary_ind(self, ind):
        required_bits_cnt = self.__calculate_required_bits_for_states()
        binary_result = f"{required_bits_cnt}\'b"
        binary_ind = ""
        while ind != 0:
            binary_ind += str(ind % 2)
            ind = ind // 2
        binary_ind = binary_ind[::-1]
        binary_result += "0" * (required_bits_cnt - len(binary_ind)) + binary_ind
        return binary_result

    def __generate_module_definition_code(self, module_name):
        port_list = "clk, rst"
        for input_port in self.fsm.get_inputs():
            port_list += f", {input_port}"
        for output_port in self.fsm.get_outputs():
            port_list += f", {output_port}"
        self.__verilog_code += f"module {module_name}({port_list});\n\n"

    def __generate_module_input_definition_code(self):
        input_definition_code = "input clk, rst, "
        input_definition_code += ", ".join(self.fsm.get_inputs())
        self.__verilog_code += input_definition_code + ";\n"

    def __generate_module_output_definition_code(self):
        output_definition_code = "output "
        output_definition_code += ", ".join(self.fsm.get_outputs())
        self.__verilog_code += output_definition_code + ";\n\n"

    def __generate_state_definition_code(self):
        state_definition_code = "localparam "
        fsm_states = self.fsm.get_states()
        for i in range(len(fsm_states)):
            cur_state = fsm_states[i]
            state_definition_code += f"{cur_state.get_name()} = {self.__get_binary_ind(i)}"
            if i != len(fsm_states) - 1:
                state_definition_code += ", "

        self.__verilog_code += state_definition_code + ";\n\n"

    def __generate_ns_ps_definition_code(self):
        required_bits_cnt = self.__calculate_required_bits_for_states()
        ns_ps_code = f"reg [{required_bits_cnt - 1}:0] ns, ps"
        self.__verilog_code += ns_ps_code + ";\n\n"

    def __get_ns_update_case_items(self):
        case_items = []
        fsm_states = self.fsm.get_states()
        initial_state_name = self.fsm.get_initial_state().get_name()

        for cur_state in fsm_states:
            cur_state_transitions = self.fsm.get_state_transitions(cur_state)
            first_cond_flag = True
            body = ""
            for cur_transition in cur_state_transitions:
                end_state_name = cur_transition.get_end_state().get_name()
                if first_cond_flag:
                    body += f"if ({cur_transition.get_condition()})\n  ns <= {end_state_name};\n"
                    first_cond_flag = False
                else:
                    body += f"else if ({cur_transition.get_condition()})\n  ns <= {end_state_name};\n"
            body += f"else\n  ns <= {cur_state.get_name()};"
            case_items.append(self.__case_item_generator.generate_code(cur_state.get_name(), body))
        case_items.append(self.__case_item_generator.generate_code("default", f"ns <= {initial_state_name};"))
        return case_items

    def __generate_ns_update_part_code(self):
        ns_update_code = ""
        always_ports = ["ps"]
        for input_name in self.fsm.get_inputs():
            always_ports.append(input_name)
        always_body = self.__case_generator.generate_code(["ps"], self.__get_ns_update_case_items())
        ns_update_code += self.__always_generator.generate_code(ports=always_ports, body_code=always_body)
        self.__verilog_code += ns_update_code

    def __get_output_assign_code(self, output_ind):
        output_assign_code = ""
        fsm_states = self.fsm.get_states()
        for state in fsm_states:
            if state.get_outputs()[output_ind]:
                output_assign_code += f"(ps=={state.get_name()})? 1\'b1: "
        return output_assign_code

    def __generate_assign_part_code(self):
        assign_code = ""
        fsm_outputs = self.fsm.get_outputs()
        for output_ind in range(len(fsm_outputs)):
            output = fsm_outputs[output_ind]
            assign_code += f"assign {output} = "
            assign_code += self.__get_output_assign_code(output_ind)
            assign_code += "1\'b0;\n"
        self.__verilog_code += assign_code + "\n"

    def __generate_clk_control_part_code(self):
        clk_control_code = ""
        always_ports = ["posedge clk", "posedge rst"]
        always_body = f"if (rst) ps <= {self.fsm.get_initial_state().get_name()};\nelse ps <= ns;\n"
        clk_control_code += self.__always_generator.generate_code(always_ports, always_body)
        self.__verilog_code += clk_control_code

    def __generate_verilog_module_body_code(self):
        self.__generate_module_input_definition_code()
        self.__generate_module_output_definition_code()
        self.__generate_state_definition_code()
        self.__generate_ns_ps_definition_code()
        self.__generate_ns_update_part_code()
        self.__generate_assign_part_code()
        self.__generate_clk_control_part_code()

    def __generate_verilog_module_code(self, module_name):
        self.__generate_module_definition_code(module_name)
        self.__generate_verilog_module_body_code()
        self.__verilog_code += "endmodule\n"

    def generate(self, module_name):
        self.__verilog_code = self.EMPTY
        self.__generate_verilog_module_code(module_name)

    def get_verilog_code(self):
        return self.__verilog_code
