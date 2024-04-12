"""test"""
from calculator import Addition, Soustraction, Division

def test_addition():
    """test"""
    calc = Addition(1, 1)
    assert calc.calculate() == 2

def test_soustraction():
    """test"""
    calc = Soustraction(1, 1)
    assert calc.calculate() == 0

def test_division():
    """test"""
    calc = Division(4, 2)
    assert calc.calculate() == 2
