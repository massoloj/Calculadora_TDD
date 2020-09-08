from source import constants as limits


class OperationException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class MinimumLimitException(Exception):
    def __init__(self):
        message = f'The minimum allowed value is {limits.MINIMUM_LIMIT}'
        super().__init__(message)


class MaximumLimitException(Exception):
    def __init__(self):
        message = f'The maximum allowed value is {limits.MAXIMUM_LIMIT}'
        super().__init__(message)


class ValueNotIntegerException(Exception):
    def __init__(self):
        message = 'Only integer values are allowed'
        super().__init__(message)
