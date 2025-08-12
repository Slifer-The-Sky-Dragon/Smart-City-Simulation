from fsm import FSM
from exceptions import *


class FSMParser:
    STATES_IND = 0
    INPUTS_IND = 1
    OUTPUTS_IND = 2
    INITIAL_STATE_IND = 3
    TRANSITIONS_IND = 4

    def __init__(self):
        self.__fsm = FSM()
        self.__parse_state = None
        self.__parse_states_names = {"STATES": 0, "INPUTS": 1, "OUTPUTS": 2, "INITIAL_STATE": 3, "TRANSITIONS": 4}
        self.__cur_state_name = None

    def __clear(self):
        self.__fsm.clear()

    def __update_parse_state(self, line):
        new_parse_state_trig = line[0]
        if new_parse_state_trig in self.__parse_states_names.keys():
            self.__parse_state = self.__parse_states_names[new_parse_state_trig]
            return 1
        return -1

    def __parse_line(self, line):
        if self.__update_parse_state(line) == 1:
            return
        if self.__parse_state == self.STATES_IND:
            new_state_name = line[0]
            new_state_outputs = list(map(int, line[1:]))
            self.__fsm.add_state(new_state_name, new_state_outputs)
        elif self.__parse_state == self.INPUTS_IND:
            self.__fsm.set_inputs(line)
        elif self.__parse_state == self.OUTPUTS_IND:
            self.__fsm.set_outputs(line)
        elif self.__parse_state == self.INITIAL_STATE_IND:
            initial_state_name = line[0]
            self.__fsm.set_initial_state(initial_state_name)
        elif self.__parse_state == self.TRANSITIONS_IND:
            if len(line) == 1:
                self.__cur_state_name = line[0]
            else:
                line = " ".join(line).split("->")
                self.__fsm.add_state_transition(self.__cur_state_name, line[1][1:], line[0][:-1])
        else:
            raise InvalidParserState

    def parse_file(self, file_path):
        self.__clear()
        with open(file_path, "r") as fsm_file:
            all_lines = fsm_file.readlines()
            for line in all_lines:
                clean_line = line.rstrip().replace(":", "").replace(",", "").split()[1:]
                if len(clean_line) > 0:
                    self.__parse_line(clean_line)

    def get_fsm(self):
        return self.__fsm
