"""
Создать файл matrix.py. Создать класс Matrix.
Атрибуты - data(содержит саму матрицу - список списков),
n,
m.
Определить конструктор
(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b),
по-умолчанию(матрица 5 на 5 где все элементы равны нулю), копирования) ,
переопределить магический метод __str__ для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix.
Функции позволяют искать максимальный элемент матрицы, минимальный, сумму всех элементов.
Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами
"""

from random import randint


class Matrix:
    def __init__(self, data=None, n=5, m=5, a=0, b=0):
        if data:
            self.__n = data.__n
            self.__m = data.__m
            self.__data = data.__data
        else:
            self.__n = n
            self.__m = m
            self.__data = [[randint(a, b) for element in range(m)] for row in range(n)]

    def __str__(self):
        return f"{self.__data}"

    @property
    def data(self):
        return self.__data

    def max_element(self):
        element = max([max(row) for row in self.__data])
        return element

    def min_element(self):
        element = min([min(row) for row in self.__data])
        return element

    def sum_matrix(self):
        sum_matrix = sum([sum(row) for row in self.__data])
        return sum_matrix


def matrix_max_element(mat: Matrix):
    element = max([max(row) for row in mat.data])
    return element


def matrix_min_element(mat: Matrix):
    element = min([min(row) for row in mat.data])
    return element


def matrix_sum_matrix(mat: Matrix):
    sum_matrix = sum([sum(row) for row in mat.data])
    return sum_matrix
