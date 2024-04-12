from calculator import addition
from calculator import soustraction
from calculator import division


def test_addition():
    calc = addition(1, 1)
    assert calc.addition() == 2

def test_soustraction():
    calc = soustraction(1, 1)
    assert calc.soustraction() == 0

def test_division():
    calc = division(4, 2)
    assert calc.division() == 2
