import sys
sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_03 as func


def test_fact():
    assert func.factorial(3) == 6


def test_neg_fact():
    assert func.factorial(-1) == -1


def test_zero_fact():
    assert func.factorial(0) == 1
