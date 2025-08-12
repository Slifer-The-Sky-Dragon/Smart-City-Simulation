class DuplicateStateName(Exception):
    """Raised when an duplicate state is being added to the fsm"""


class StateNotFound(Exception):
    """Raised when a state is not found in our FSM"""


class InvalidParserState(Exception):
    """Raised when the parser state is not valie"""
