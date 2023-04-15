import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_04 as func


def test_get_arr_right_size():
    arr = func.fillArr(3)
    assert len(arr) == 3 and [3, 3, 3] == [len(row) for row in arr]


def test_lower_range():
    arr = func.fillArr(3, random_from=2)
    for row in arr:
        lowest = min(row)
    assert lowest >= 2


def test_higher_range():
    arr = func.fillArr(3, random_to=5)
    for row in arr:
        highest = max(row)
    assert highest <= 5


def test_both_ranges():
    arr = func.fillArr(3, random_from=3, random_to=5)
    for row in arr:
        highest = max(row)
        lowest = min(row)
    assert highest <= 5 and lowest >= 3
