import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_12 as func
import random


def test_mixed():
    A = [1, 2, -1, -2, 50, -3]
    Apos = []
    Aneg = []
    for number in A:
        if number >= 0:
            Apos.append(number)
        else:
            Aneg.append(number)
    assert func.summArr(*Apos) == 53 and func.summArr(*Aneg) == -6

def test_all_neg():
    A = [-1, -2, -3]
    Apos = []
    Aneg = []
    for number in A:
        if number >= 0:
            Apos.append(number)
        else:
            Aneg.append(number)
    assert func.summArr(*Apos) == 0 and func.summArr(*Aneg) == -6

def test_all_pos():
    A = [1, 2, 3]
    Apos = []
    Aneg = []
    for number in A:
        if number >= 0:
            Apos.append(number)
        else:
            Aneg.append(number)
    assert func.summArr(*Apos) == 6 and func.summArr(*Aneg) == 0
