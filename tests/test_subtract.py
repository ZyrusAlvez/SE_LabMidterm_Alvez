import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from model.calculator import calculator


def test_subtract():
    assert calculator.subtract(10, 4) == 6

def test_subtract_negative():
    assert calculator.subtract(3, 7) == -4

def test_subtract_floats():
    assert calculator.subtract(5.5, 2.5) == 3.0

def test_subtract_string():
    with pytest.raises(TypeError):
        calculator.subtract(5, "2")
