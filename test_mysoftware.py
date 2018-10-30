from mysoftware import *

def test_square_integers():
    assert square(1) == 1
    assert square(2) == 4
    assert square(4) == 16
    assert square(-1) == 1

def test_coulomb():
    assert coulomb(1) == 1
    assert coulomb(-1) == 1
    assert (coulomb(2) - 0.5) < 1.0e-10
    assert coulomb(2) == 0.5
    assert coulomb(0.5) == 2
    assert coulomb(10) == 0.1



def test_coulomb_failed():
    try:
        coulomb(0.0)
        raise Exception("Test failed")
    except:
        pass
