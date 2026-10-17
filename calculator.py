"""Core Calculator implementation."""

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        """Adds two numbers and stores in history."""
        res = a + b
        self.history.append(("add", a, b, res))
        return res

    def subtract(self, a: float, b: float) -> float:
        """Subtracts b from a."""
        res = a - b
        self.history.append(("sub", a, b, res))
        return res

    def divide(self, a: float, b: float) -> float:
        """Divides a by b. Raises ValueError on zero division."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        res = a / b
        self.history.append(("div", a, b, res))
        return res
