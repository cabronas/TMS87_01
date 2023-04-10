import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_08 as func


def test_mean_1():
    result = func.sred(1, 2, 3, 4, mean_type=1)
    assert result == 2.5


def test_mean_2():
    result = func.sred(1, 2, 3, 4, mean_type=2)
    assert round(result, 2) == 2.21


def test_sredAr():
    result = func.sredAr(-2, 2)
    assert result == 0


def test_sredGe():
    result = func.sredAr(-2, 2)
    assert result == 0
