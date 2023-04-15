import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_05 as func


def test_pos():
    result = func.summArr(4, 3, 2, 1)
    assert result == 10


def test_neg():
    result = func.summArr(-1, -2)
    assert result == -2


def test_zero():
    result = func.summArr(0, 0)
    assert result == 0
