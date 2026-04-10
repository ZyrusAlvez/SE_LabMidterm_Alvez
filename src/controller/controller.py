import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from model.calculator import calculator

OPERATORS = {"+", "−", "×", "÷"}


class Controller:
    def __init__(self, view):
        self._view       = view
        self._operand_a  = None
        self._operator   = None
        self._reset_next = False

    def on_button(self, label: str):
        if label == "DEL":
            self._handle_del()
        elif label == "=":
            self._handle_equals()
        elif label in OPERATORS:
            self._handle_operator(label)
        else:
            self._handle_digit(label)

    def _is_error(self) -> bool:
        return self._view.get_display().startswith("Error")

    def _handle_digit(self, label: str):
        current = self._view.get_display()
        if self._reset_next or current == "0" or self._is_error():
            current = ""
            self._reset_next = False
        if label == "." and "." in current:
            return
        self._view.set_display(current + label)

    def _handle_operator(self, label: str):
        if self._is_error():
            return
        if self._operand_a is not None and not self._reset_next:
            self._compute()
            if self._is_error():
                return
        self._operand_a  = float(self._view.get_display())
        self._operator   = label
        self._reset_next = True
        self._view.set_expression(f"{self._format(self._operand_a)} {label}")

    def _handle_equals(self):
        if self._operand_a is None or self._operator is None:
            return
        if self._is_error():
            return
        self._view.set_expression(
            f"{self._format(self._operand_a)} {self._operator} {self._view.get_display()} ="
        )
        self._compute()
        self._operand_a  = None
        self._operator   = None
        self._reset_next = True

    def _handle_del(self):
        current = self._view.get_display()
        if self._is_error():
            self._view.set_display("0")
            self._view.set_expression("")
            self._reset_state()
            return
        self._view.set_display(current[:-1] if len(current) > 1 else "0")

    def _compute(self):
        try:
            a, b = self._operand_a, float(self._view.get_display())

            if self._operator == "+":
                result = calculator.add(a, b)
            elif self._operator == "−":
                result = calculator.subtract(a, b)
            elif self._operator == "×":
                result = calculator.multiply(a, b)
            elif self._operator == "÷":
                result = calculator.divide(a, b)

            self._view.set_display(self._format(result))

        except (ZeroDivisionError, TypeError) as e:
            self._view.set_error(e)
            self._reset_state()

    def _format(self, value: float) -> str:
        return str(int(value)) if value == int(value) else str(value)

    def _reset_state(self):
        self._operand_a  = None
        self._operator   = None
        self._reset_next = True
        self._view.set_expression("")
