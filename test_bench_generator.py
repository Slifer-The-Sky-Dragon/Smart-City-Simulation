from fsm import FSM
from copy import deepcopy
from verilog_generator import VerilogInitialGenerator


class FSMPathExtractor:
    def __init__(self, fsm: FSM):
        self.__fsm = fsm
        self.__paths = []
        self.__state_mark = {}

    def __DFS(self, cur_state, transitions, cur_path):
        self.__state_mark[cur_state] = True
        for i in range(len(transitions[cur_state])):
            cur_transition = transitions[cur_state][i]
            new_state = cur_transition.get_end_state()
            transition_condition = cur_transition.get_condition()
            if new_state not in self.__state_mark.keys():
                new_path = deepcopy(cur_path)
                new_path.append([new_state, transition_condition])
                self.__DFS(new_state, transitions, new_path)
            else:
                new_path = deepcopy(cur_path)
                new_path.append([new_state, transition_condition])
                self.__paths.append(new_path)
        if len(transitions[cur_state]) == 0:
            self.__paths.append(cur_path)

    def extract(self):
        fsm_transitions = self.__fsm.get_transitions()
        start_state = self.__fsm.get_initial_state()
        self.__DFS(start_state, fsm_transitions, [])

    def get_paths(self):
        return self.__paths


class VerilogTestBenchGenerator:
    EMPTY = ""

    def __init__(self, fsm: FSM):
        self.__fsm = fsm
        self.__path_extractor = FSMPathExtractor(fsm)
        self.__verilog_initial_generator = VerilogInitialGenerator(indent_lvl=2)
        self.__verilog_code = self.EMPTY

    def __generate_reg_definition_code(self):
        reg_definition_code = "reg clk, rst, "
        reg_definition_code += ", ".join(self.__fsm.get_inputs())
        self.__verilog_code += reg_definition_code + ";\n"

    def __generate_wire_definition_code(self):
        wire_definition_code = "wire "
        wire_definition_code += ", ".join(self.__fsm.get_outputs())
        self.__verilog_code += wire_definition_code + ";\n\n"

    def __generate_fsm_instance_code(self, module_name):
        fsm_instance_code = f"{module_name} test_fsm(clk, rst, "
        fsm_instance_code += ", ".join(self.__fsm.get_inputs()) + ", "
        fsm_instance_code += ", ".join(self.__fsm.get_outputs())
        fsm_instance_code += ")"
        self.__verilog_code += fsm_instance_code + ";\n\n"

    def __generate_input_initialization_code(self):
        input_initial_body_code = ""
        all_fms_inputs = self.__fsm.get_inputs()
        for i in range(len(all_fms_inputs)):
            cur_input = all_fms_inputs[i]
            input_initial_body_code += f"{cur_input} = 0;"
            if i != len(all_fms_inputs) - 1:
                input_initial_body_code += "\n"
        self.__verilog_code += self.__verilog_initial_generator.generate_code(input_initial_body_code)

    def __get_path_test_case_code(self, path):
        test_case_code = "#10 rst=1;\n#10 rst=0;\n"
        for path_transition_info in path:
            path_transition_condition = path_transition_info[1]
            transition_conditions = path_transition_condition.split("&")
            test_case_code += "#10\n  clk=0;\n"
            mark_active_inputs = {}
            for input_name in transition_conditions:
                input_name = input_name.replace(" ", "")
                if "!" not in input_name:
                    mark_active_inputs[input_name] = 1
            for input_name in self.__fsm.get_inputs():
                if input_name in mark_active_inputs.keys():
                    test_case_code += f"  {input_name} = 1;\n"
                else:
                    test_case_code += f"  {input_name} = 0;\n"
            test_case_code += "#10  clk=1;\n"
        return test_case_code + "\n"

    def __generate_test_part_code(self, paths):
        test_initial_body_code = ""
        for path in paths:
            test_initial_body_code += self.__get_path_test_case_code(path)
        self.__verilog_code += self.__verilog_initial_generator.generate_code(test_initial_body_code)

    def __generate_test_bench_body_code(self, paths, module_name):
        self.__generate_reg_definition_code()
        self.__generate_wire_definition_code()
        self.__generate_fsm_instance_code(module_name)
        self.__generate_input_initialization_code()
        self.__generate_test_part_code(paths)

    def __generate_test_bench_module_code(self, paths, module_name):
        self.__verilog_code += f"module {module_name}_test_bench();\n\n"
        self.__generate_test_bench_body_code(paths, module_name)
        self.__verilog_code += "endmodule"

    def generate(self, module_name):
        self.__path_extractor.extract()
        paths = self.__path_extractor.get_paths()
        self.__generate_test_bench_module_code(paths, module_name)

    def get_code(self):
        return self.__verilog_code
