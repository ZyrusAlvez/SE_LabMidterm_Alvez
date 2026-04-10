import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from model.calculator import calculator


def test_divide():
    assert calculator.divide(10, 2) == 5.0

def test_divide_floats():
    assert calculator.divide(7.5, 2.5) == 3.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)

def test_divide_string():
    with pytest.raises(TypeError):
        calculator.divide(10, "2")
