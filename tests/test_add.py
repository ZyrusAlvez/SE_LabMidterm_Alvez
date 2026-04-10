import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from model.calculator import calculator


def test_add():
    assert calculator.add(2, 3) == 5

def test_add_floats():
    assert calculator.add(1.5, 2.5) == 4.0

def test_add_negative():
    assert calculator.add(-1, -2) == -3

def test_add_string():
    with pytest.raises(TypeError):
        calculator.add("1", 2)

def test_add_bool():
    with pytest.raises(TypeError):
        calculator.add(True, 1)
