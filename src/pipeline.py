

class BasicOperations:
    def __init__(self):
        pass
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    def multiply(self, a, b):
        """Multiply b by a number."""
        return a * b
    def divide(self, a, b):
        """Divide b by a number."""
        return a / b if b != 0 else 0
