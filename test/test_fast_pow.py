import pytest
from src.fast_pow import fastPow


def test_two_power_two():
    assert fastPow(2, 2) == 4


def test_negative():
    assert fastPow(-1, 4) == 1
    

def test_power_zero():
    assert fastPow(58, 0) == 1
    

def test_odd_degree():
    assert fastPow(2, 5) == 32
    
    
def test_negative_power():
    with pytest.raises(ValueError, match="Введена отрицательная степень"):
        fastPow(2, -1)
