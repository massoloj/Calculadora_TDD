from source.exceptions import OperationException


class Calculator:
    def __init__(self):
        pass

    @classmethod
    def add(cls, value1, value2):
        try:
            return value1 + value2
        except Exception as e:
            raise OperationException(
                message='There was an error in sum operation',
                errors=e
            )

    @classmethod
    def substract(cls, value1, value2):
        pass

    @classmethod
    def multiply(cls, value1, value2):
        pass

    @classmethod
    def divide(cls, value1, value2):
        pass
