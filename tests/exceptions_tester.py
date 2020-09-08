import unittest

from source.value_validator import ValueValidator
from source.exceptions import(
    MinimumLimitException,
    MaximumLimitException,
    ValueNotIntegerException
)

from source import constants as limits


class ValueValidatorTester(unittest.TestCase):

    def setUp(self):
        self.value_validator = ValueValidator()

    def test_value_validator_raises_value_not_integer_exception(self):
        test_value = 1.0
        expected_exception = ValueNotIntegerException
        expected_message = 'Only integer values are allowed'

        with self.assertRaises(expected_exception) as context:
            self.value_validator.validate_value(test_value)

        self.assertTrue(expected_message in str(context.exception))

    def test_value_validator_raises_minimum_limit_exception(self):
        test_value = 1
        expected_exception = MinimumLimitException
        expected_message = f'The minimum allowed value is {limits.MINIMUM_LIMIT}'

        with self.assertRaises(expected_exception) as context:
            self.value_validator.validate_value(test_value)

        self.assertTrue(expected_message in str(context.exception))

    def test_value_validator_raises_maximum_limit_exception(self):
        test_value = 150
        expected_exception = MaximumLimitException
        expected_message = f'The maximum allowed value is {limits.MINIMUM_LIMIT}'

        with self.assertRaises(expected_exception) as context:
            self.value_validator.validate_value(test_value)

        self.assertTrue(expected_message in str(context.exception))

