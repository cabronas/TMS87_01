import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_07 as func


def test_default():
    result = func.evenKey(a=1, ab=2, abc=3, abcd=4)
    assert result == {"ab": 2, "abcd": 4}


def test_short():
    result = func.evenKey(a=1)
    assert result == {}
