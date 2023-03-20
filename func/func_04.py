"""
Реализовать функцию возвращающую матрицу.
На вход принимает n - размерность матрицы,
random_from(по-умолчанию 1),
random_to(по-умолчанию(9)).
"""
import random


def fillArr(n, random_from=1, random_to=9):
    resultArr = []
    for i in range(n):
        column = []
        for j in range(n):
            column.append(random.randint(random_from, random_to))
        resultArr.append(column)
    return resultArr


dimensions = input("n=")
print(fillArr(3))
