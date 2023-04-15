import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_10 as func


def test_descriminator_pos():
    result = func.descriminator(1, 1, 1)
    assert result == -3


def test_descriminator_neg():
    result = func.descriminator(-2, -1, -5)
    assert result == -39


def test_descriminator_mixed():
    result = func.descriminator(-2, -1, 5)
    assert result == 41


def test_rootfinder_pos():
    assert func.rootFinder(2, 3, 1, 1) == -0.5 and func.rootFinder(2, 3, 1, -1) == -1


def test_rootfinder_neg():
    assert func.rootFinder(-2, -3, 1, 1) == -1 and func.rootFinder(-2, -3, 1, -1) == -0.5
