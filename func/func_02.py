"""
Написать программу для работы с матрицами:
Создание
Вывод
Сумма всех элементов
Нахождение максимального элемента
Нахождение минимального элемента.
"""
import random

array = []


def fillMat():
    arr = [random.randint(1, 10) for i in range(10)]
    return arr

def printMat(arr):
    print(*arr)


def summAll(arr):
    summ = 0
    for number in arr:
        summ += number
    return summ

def findMax(arr):
    return max(arr)
def findMin(arr):
    return min(arr)
def main():
    array = fillMat()
    printMat(array)
    print(summAll(array))
    print(findMax(array))
    print(findMin(array))
main()
