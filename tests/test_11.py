import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_13 as func
import random


def test_int():
    result = func.convertMeasurments(1, 2)
    assert result == 2


def test_float():
    result = func.convertMeasurments(1.1, 2.2)
    assert round(result, 2) == 2.42


def test_negative_1():
    result = func.convertMeasurments(-1.1, -2.2)
    assert round(result, 2) == 2.42


def test_negative_2():
    result = func.convertMeasurments(-1.1, 2.2)
    assert round(result, 2) == -2.42
