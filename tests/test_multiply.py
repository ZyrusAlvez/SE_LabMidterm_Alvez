import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from model.calculator import calculator


def test_multiply():
    assert calculator.multiply(3, 4) == 12

def test_multiply_by_zero():
    assert calculator.multiply(5, 0) == 0

def test_multiply_floats():
    assert calculator.multiply(2.5, 4) == 10.0

def test_multiply_string():
    with pytest.raises(TypeError):
        calculator.multiply("a", 3)
