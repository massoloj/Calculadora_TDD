
class Calculator:
    def __init__(self):
        pass

    def add(self, value1, value2):
        try:
            return value1 + value2
        except Exception as error:
            raise error('Error in addition')

    def substract(self, value1, value2):
        pass

    def multiply(self, value1, value2):
        pass

    def divide(self, value1, value2):
        pass
