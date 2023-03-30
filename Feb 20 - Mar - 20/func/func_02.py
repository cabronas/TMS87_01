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
    arr = [
        [
            random.randint(0, 9) for i in range(4)
        ]
        for i in range(4)
    ]
    return arr


def printMat(arr):
    for numberArr in arr:
        print(*numberArr)


def summAll(arr):
    summ = 0
    for numberArr in arr:
        for number in numberArr:
            summ += number
    return summ


def findMax(arr):
    maximum = arr[0][0]
    for numberArr in arr:
        if maximum < max(numberArr):
            maximum = max(numberArr)
    return maximum

def findMin(arr):
    minimum = arr[0][0]
    for numberArr in arr:
        if minimum > min(numberArr):
            minimum = min(numberArr)
    return minimum


def main():
    array = fillMat()
    printMat(array)
    print(summAll(array))
    print(findMax(array))
    print(findMin(array))


if __name__ == "__main__":
    main()
