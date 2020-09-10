from source.decorators import input_validator
from source.exceptions import OperationException


class Calculator:
    def __init__(self):
        pass

    @classmethod
    @input_validator
    def add(cls, value1, value2):
        try:
            return value1 + value2
        except Exception as e:
            raise OperationException(
                message='There was an error in sum operation',
                errors=e
            )

    @classmethod
    @input_validator
    def substract(cls, value1, value2):
        try:
            return value1 - value2
        except Exception as e:
            raise OperationException(
                message='There was an error in substract operation',
                errors=e
            )

    @classmethod
    @input_validator
    def multiply(cls, value1, value2):
        try:
            return value1 * value2
        except Exception as e:
            raise OperationException(
                message='There was an error in multiply operation',
                errors=e
            )

    @classmethod
    def divide(cls, value1, value2):
        pass
