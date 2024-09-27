from typing import Self

class DomainBaseException(Exception):
    def __init__(self: Self, message: str) -> None:
        self.message: str = message


class ValidationError(DomainBaseException):
    pass