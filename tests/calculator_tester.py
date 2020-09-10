import unittest

from source.calculator import Calculator
from source.exceptions import (
    OperationException,
    MinimumLimitException,
    ValueNotIntegerException
)


class CalculatorTester(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_success(self):
        test_value1 = 10
        test_value2 = 100
        expected_result = 110

        result = self.calculator.add(test_value1, test_value2)
        assert result == expected_result

    def test_add_raises_value_not_integer_exception(self):
        test_value1 = 10
        test_value2 = '1'
        expected_exception = ValueNotIntegerException
        expected_message = 'Only integer values are allowed'

        with self.assertRaises(expected_exception) as context:
            self.calculator.add(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))

    def test_add_raises_minimum_limit_exception(self):
        test_value1 = 1
        test_value2 = 10
        expected_exception = MinimumLimitException
        expected_message = 'The minimum allowed value is 10'

        with self.assertRaises(expected_exception) as context:
            self.calculator.add(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))

    def test_substract_success(self):
        test_value1 = 60
        test_value2 = 50
        expected_result = 10

        result = self.calculator.substract(test_value1, test_value2)
        assert result == expected_result

    def test_substract_raises_value_not_integer_exception(self):
        test_value1 = 10
        test_value2 = '1'
        expected_exception = ValueNotIntegerException
        expected_message = 'Only integer values are allowed'

        with self.assertRaises(expected_exception) as context:
            self.calculator.substract(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))

    def test_substract_raises_minimum_limit_exception(self):
        test_value1 = 100
        test_value2 = 1
        expected_exception = MinimumLimitException
        expected_message = 'The minimum allowed value is 10'

        with self.assertRaises(expected_exception) as context:
            self.calculator.substract(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))

    def test_multiply_success(self):
        test_value1 = 100
        test_value2 = 100
        expected_result = 10000

        result = self.calculator.multiply(test_value1, test_value2)
        assert result == expected_result

    def test_multiply_raises_value_not_integer_exception(self):
        test_value1 = 100
        test_value2 = '1'
        expected_exception = ValueNotIntegerException
        expected_message = 'Only integer values are allowed'

        with self.assertRaises(expected_exception) as context:
            self.calculator.multiply(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))

    def test_multiply_raises_minimum_limit_exception(self):
        test_value1 = 100
        test_value2 = 1
        expected_exception = MinimumLimitException
        expected_message = 'The minimum allowed value is 10'

        with self.assertRaises(expected_exception) as context:
            self.calculator.multiply(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))

    def test_divide_success(self):
        test_value1 = 100
        test_value2 = 100
        expected_result = 1

        result = self.calculator.divide(test_value1, test_value2)
        assert result == expected_result

    def test_divide_raises_value_not_integer_exception(self):
        test_value1 = 100
        test_value2 = '1'
        expected_exception = ValueNotIntegerException
        expected_message = 'Only integer values are allowed'

        with self.assertRaises(expected_exception) as context:
            self.calculator.divide(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))

    def test_divide_raises_minimum_limit_exception(self):
        test_value1 = 100
        test_value2 = 1
        expected_exception = MinimumLimitException
        expected_message = 'The minimum allowed value is 10'

        with self.assertRaises(expected_exception) as context:
            self.calculator.divide(test_value1, test_value2)

        self.assertTrue(expected_message in str(context.exception))


if __name__ == '__main__':
    unittest.main()
