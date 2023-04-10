import sys

sys.path.append('E:\\DELLATER\\PYCHARMPROJ\\Feb20Mar20\\func')
import func_15 as func
import random


def test_list():
    # text_file = open('tests/zaliznyak.txt')
    # polydromes = [line[:-1] for line in text_file]
    # text_file.close()
    polydromes = ["a", "aba", "abbbba", "bdbdb"]
    check = True
    for polydrome in polydromes:
        if not func.checkIfPolyndrom(polydrome):
            print(polydrome)
            check = False
    assert check


def test_notpoly():
    assert not func.checkIfPolyndrom("bba")
