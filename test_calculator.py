from calculator import Addition
from calculator import Soustraction
from calculator import Division


def test_addition():
    calc = Addition(1, 1)
    assert calc.addition() == 2

def test_soustraction():
    calc = Soustraction(1, 1)
    assert calc.soustraction() == 0

def test_division():
    calc = Division(4, 2)
    assert calc.division() == 2
