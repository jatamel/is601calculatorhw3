'''my calculator test'''
from calculator import add, subtract

def test_addition():
    "test that addition function works"
    assert add(2,2) == 4

def test_subrtaction():
    "test that subtraction function works"
    assert subtract(2,2) == 0

def test_multiply():
    "test that multiplication function works"
    assert multiply(2,3) == 6

def test_divide():
    "test that multiplication function works"
    assert divide(3,3) == 1