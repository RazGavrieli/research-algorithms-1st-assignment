from outcome import capture
import pytest
from sortedPrint import *

def test_1(capsys):
    x = {'a':5, 'c':{4, 3, 6}, 'b': [[3,2], [12, 32, 1,3], [5]]}
    print_sorted(x)
    captured = capsys.readouterr()
    assert captured.out == "a: 5 b: 2 3 5 1 3 12 32 c: 3 4 6 "

def test_2(capsys):
    x = [1, 2, {'c':[3, 2, 1], 'a': {2: 'world', 1:'hello'}, 'g':4}]
    print_sorted(x)
    captured = capsys.readouterr()
    assert captured.out == "1 2 a: 1: hello 2: world c: 1 2 3 g: 4 "

def test_3(capsys):
    x = [1, 4, 2, 3]
    print_sorted(x)
    captured = capsys.readouterr()
    assert captured.out == "1 2 3 4 "

def test_4(capsys):
    x = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print_sorted(x)
    captured = capsys.readouterr()
    assert captured.out == "a: 5 b: 1 2 3 4 c: 6 "