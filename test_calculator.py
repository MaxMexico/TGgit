from calculator import addition
from calculator import soustraction
from calculator import division

def test_addition():
    assert addition(1, 1) == 2

def test_soustraction():
    assert soustraction(1, 1) == 0

def test_division():
    assert division(4, 2) == 2