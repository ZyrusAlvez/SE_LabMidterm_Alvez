class Calculator:
    def _validate(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Operands must be numeric, got {type(a).__name__} and {type(b).__name__}")
        if isinstance(a, bool) or isinstance(b, bool):
            raise TypeError("Boolean values are not allowed as operands")

    def add(self, a, b):
        self._validate(a, b)
        return a + b

    def subtract(self, a, b):
        self._validate(a, b)
        return a - b

    def multiply(self, a, b):
        self._validate(a, b)
        return a * b

    def divide(self, a, b):
        self._validate(a, b)
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
    
calculator = Calculator()