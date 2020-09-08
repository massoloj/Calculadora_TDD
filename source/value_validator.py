from source import constants as limits
from source.exceptions import(
    MaximumLimitException,
    MinimumLimitException,
    ValueNotIntegerException
)


class ValueValidator:
    @staticmethod
    def _validate_value_is_int(value):
        if not isinstance(value, int):
            raise ValueNotIntegerException()

    @staticmethod
    def _validate_minimum_limit(value):
        if value < limits.MINIMUM_LIMIT:
            raise MinimumLimitException()

    @staticmethod
    def _validate_maximum_limit(value):
        if value > limits.MAXIMUM_LIMIT:
            raise MaximumLimitException()

    @staticmethod
    def validate_value(value):
        ValueValidator._validate_value_is_int(value)
        ValueValidator._validate_minimum_limit(value)
        ValueValidator._validate_maximum_limit(value)
