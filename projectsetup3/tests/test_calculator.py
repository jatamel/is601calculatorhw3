'''my calculator test'''
from calculator import add, subtract

def test_addition():
    '''meep porp this is a test addition function'''
    assert add(2,2) == 4

def test_subrtaction():
    '''meep porp this is a test subtract function'''
    assert subtract(2,2) == 0
