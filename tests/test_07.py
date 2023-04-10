import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_09 as func


def test_pos():
    result = func.getOcc([1, 2, 2])
    assert result == {1: 1, 2: 2}

def test_all_unique():
    result = func.getOcc([1, 2, 3])
    assert result == {1: 1, 2: 1, 3: 1}

def test_empty():
    result = func.getOcc([])
    assert result == {}
