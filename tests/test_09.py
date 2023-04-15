import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_11 as func


def test_power_true():
    result = func.is_power_n(4, 2)
    assert result


def test_power_false():
    result = func.is_power_n(2, 4)
    assert not result

def test_power_negative():
    result = func.is_power_n(-2, 4)
    assert not result