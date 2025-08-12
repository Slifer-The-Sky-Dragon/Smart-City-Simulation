from fsm_parser import FSMParser
from verilog_generator import VerilogFSMGenerator
from test_bench_generator import VerilogTestBenchGenerator
import sys


def generate_fsm_verilog(input_fsm, module_name):
    verilog_generator = VerilogFSMGenerator(input_fsm)
    verilog_generator.generate(module_name=module_name)
    return verilog_generator.get_verilog_code()


def generate_fsm_test_bench_verilog(input_fsm, module_name):
    verilog_test_bench_generator = VerilogTestBenchGenerator(input_fsm)
    verilog_test_bench_generator.generate(module_name=module_name)
    return verilog_test_bench_generator.get_code()


if __name__ == "__main__":
    fsm_file_path = sys.argv[1]
    output_verilog_file_name = sys.argv[2]

    parser = FSMParser()
    parser.parse_file(file_path=fsm_file_path)
    fsm = parser.get_fsm()

    fsm_verilog_code = generate_fsm_verilog(input_fsm=fsm, module_name=output_verilog_file_name)
    fsm_test_bench_verilog_code = generate_fsm_test_bench_verilog(input_fsm=fsm, module_name=output_verilog_file_name)

    with open(f"verilogs/{output_verilog_file_name}.v", "w+") as output_verilog_file:
        output_verilog_file.write(fsm_verilog_code)
    with open(f"verilogs/{output_verilog_file_name}_test_bench.v", "w+") as output_verilog_test_bench_file:
        output_verilog_test_bench_file.write(fsm_test_bench_verilog_code)
