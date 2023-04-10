import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_06 as func


def test_pos():
    result1, result2 = func.summMax(1, 2, 3)
    assert result1 == 6 and result2 == 3

def test_neg():
    result1, result2 = func.summMax(-1, -2)
    assert result1 == -3 and result2 == -1

def test_zero():
    result1, result2 = func.summMax(0)
    assert result1 == 0 and result2 == 0