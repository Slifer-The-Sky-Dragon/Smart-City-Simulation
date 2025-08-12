from exceptions import *


class State:
    def __init__(self, name, outputs):
        self.__name = name
        self.__outputs = outputs

    def get_name(self):
        return self.__name

    def get_outputs(self):
        return self.__outputs

    def __repr__(self):
        return self.__name

    def __str__(self):
        return f"( {self.__name}, {self.__outputs} )"


class Transition:
    def __init__(self, start_state, end_state, condition):
        self.__start_state = start_state
        self.__end_state = end_state
        self.__condition = condition

    def get_start_state(self):
        return self.__start_state

    def get_end_state(self):
        return self.__end_state

    def get_condition(self):
        return self.__condition

    def __str__(self):
        return f"( {self.__start_state.get_name()}, {self.__end_state.get_name()}, {self.__condition} )"

    def __repr__(self):
        return f"( {self.__start_state.get_name()}, {self.__end_state.get_name()}, {self.__condition} )"


class FSM:
    def __init__(self):
        self.__states = []
        self.__inputs = []
        self.__outputs = []
        self.__initial_state = None
        self.__transitions = {}

    def clear(self):
        self.__states = []
        self.__inputs = []
        self.__outputs = []
        self.__initial_state = None
        self.__transitions = {}

    def __find_state(self, state_name):
        result = None
        for state in self.__states:
            if state.get_name() == state_name:
                result = state
        return result

    def add_state(self, new_state_name, new_state_outputs):
        if self.__find_state(new_state_name) is not None:
            raise DuplicateStateName
        new_state = State(new_state_name, new_state_outputs)
        self.__states.append(new_state)
        self.__transitions[new_state] = []

    def set_inputs(self, inputs):
        self.__inputs = inputs

    def set_outputs(self, outputs):
        self.__outputs = outputs

    def set_initial_state(self, state_name):
        initial_state = self.__find_state(state_name)
        if initial_state is None:
            raise StateNotFound
        self.__initial_state = initial_state

    @staticmethod
    def __clean_condition(condition):
        condition = condition.replace(")", "")
        condition = condition.replace("(", "")
        return condition

    def add_state_transition(self, start_state_name, end_state_name, condition):
        condition = self.__clean_condition(condition)
        start_state = self.__find_state(start_state_name)
        end_state = self.__find_state(end_state_name)
        self.__transitions[start_state].append(Transition(start_state, end_state, condition))

    def get_states(self):
        return self.__states

    def get_inputs(self):
        return self.__inputs

    def get_outputs(self):
        return self.__outputs

    def get_initial_state(self):
        return self.__initial_state

    def get_transitions(self):
        return self.__transitions

    def get_state_transitions(self, state):
        return self.__transitions[state]


