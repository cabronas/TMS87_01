import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_14 as func
import random


def test_pos():
    result = func.fact2(4)
    assert result == 8


def test_neg():
    result = func.fact2(-4)
    assert result == None


def test_large():
    result = func.fact2(20)
    assert result == 3715891200

def test_zero():
    result = func.fact2(0)
    assert result == 1
