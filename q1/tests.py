from safe_call import *
import pytest

def f(x: int , y: float, z):
    return x+y+z

def g(a, b, c=3):
    return a-b-c

def h(x: int ,y: float = 3.2, z=3):
    return x+y-z

def test_exceptions_1():
    with pytest.raises(Exception) as e_info:
        safe_call(f, x=1, y=1.0, z=1, g=3)
    assert str(e_info.value) == 'unexpected arguments given to safe_call'
    
def test_exceptions_2():
    with pytest.raises(Exception) as e_info:
        safe_call(f, x=1, y=1.0)
    assert str(e_info.value) == 'missing arguments'

def test_exceptions_3():
    with pytest.raises(Exception) as e_info:
        safe_call(f, x=1, y="sbc")
    assert str(e_info.value) == 'unmatching types'

def test_exceptions_4():
    with pytest.raises(Exception) as e_info:
        safe_call(f, x=3, y=3, z=2)
    assert str(e_info.value) == 'unmatching types'

def test_exceptions_5():
    with pytest.raises(Exception) as e_info:
        safe_call(f, y=3.3, z=2)
    assert str(e_info.value) == 'missing arguments'

def test_1():
    assert safe_call(f, y=1.3, x=3, z=2) == 6.3

def test_2():
    assert safe_call(g, b=2, a=3) == -2
   