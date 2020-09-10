from .value_validator import ValueValidator


def input_validator(method):
    def method_wrapper(cls, value1, value2):
        ValueValidator.validate_value(value1)
        ValueValidator.validate_value(value2)
        return method(cls, value1, value2)

    return method_wrapper
