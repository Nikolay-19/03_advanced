class Calculator:
    def __init__(self, *args):
        self.args = args

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        result = 0
        for idx in range(len(args) - 1):
            current = args[idx]
            next1 = args[idx + 1]
            result += current / next1
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for idx in range(1, len(args)):
            current = args[idx]
            result -= current
        return result
