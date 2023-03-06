"""
Есть список arr = [1,2,3,4,4,4,5,5,2]
1. Найти сумму всех числел
2. Найти среднее арифметическое
3. Найти среднее геомнтрическое
4. Найти массив квадратов
5*. Найти кумулятивную сумму
6*. Найти медиану
7*. Найти верхнюю и нижнюю квартиль
"""
import copy
import math


def first(array):
    i = 0
    summ = 0
    while i != len(array):
        summ += arr[i]
        i += 1
    return summ


def second(array):
    i = 0
    summ = 0
    while i != len(array):
        summ += array[i]
        i += 1
    avg = summ / len(array)
    return avg


def third(array):
    i = 0
    mul = 1
    while i != len(array):
        mul *= array[i]
        i += 1
    avg = pow(mul, 1 / len(array))
    return avg


def forth(array):
    temparray = copy.copy(array)
    i = 0
    while i != len(temparray):
        temparray[i] = temparray[i] ** 2
        i += 1
    return temparray


def fifth(array):
    temparray = copy.copy(array)
    i = 0
    summ = 0
    while i != len(temparray):
        summ += temparray[i]
        temparray[i] = summ
        i += 1
    return temparray


def sixth(array):
    temparray = copy.copy(array)
    if len(array) % 2 == 0:
        median = temparray[len(temparray) / 2]
    else:
        a = len(temparray) // 2
        median = (temparray[a] + temparray[a + 1]) / 2
    return median


def seventh(array):
    temparray = copy.copy(array)
    temparray.sort()
    # # upper
    qupperpos = 0.75 * (len(temparray))
    if qupperpos % 2 != 0:
        qupperpos = math.floor(qupperpos)
        qupper = (temparray[qupperpos] + (temparray[qupperpos + 1])) / 2
    else:
        qupper = temparray[qupperpos]
    # lower
    qlowerpos = 0.25 * (len(temparray))
    if qlowerpos % 2 != 0:
        qlowerpos = math.floor(qlowerpos)
        qlower = (temparray[qlowerpos] + (temparray[qlowerpos])) / 2
    else:
        qlower = temparray[qlowerpos]
    return qupper, qlower


arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
print("1:", first(arr))
print("2:", second(arr))
print("3:", third(arr))
print("4:", *forth(arr))
print("5:", *fifth(arr))
print("6:", sixth(arr))
print("7:", *seventh(arr))
