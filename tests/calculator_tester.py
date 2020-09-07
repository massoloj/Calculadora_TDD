import unittest

from source.calculator import Calculator


class CalculatorTester(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_success(self):
        value1 = 1
        value2 = 1
        expected_result = 2

        result = self.calculator.add(value1, value2)
        assert result == expected_result

    def test_add_fails(self):
        pass

    def test_substract_success(self):
        pass

    def test_substract_fails(self):
        pass

    def test_multiply_success(self):
        pass

    def test_multiply_fails(self):
        pass

    def test_divide_success(self):
        pass

    def test_multiply_fails(self):
        pass


if __name__ == '__main__':
    unittest.main()
