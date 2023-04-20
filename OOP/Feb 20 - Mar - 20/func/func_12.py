"""
Дан массив целых чисел A.
Найти суммы положительных и отрицательных элементов массива,
используя функцию определения суммы.
"""
import random

A = []
def summArr(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


def main():
    A = [random.randint(-10, 11) for i in range(10)]
    Apos = []
    Aneg = []
    for number in A:
        if number >= 0:
            Apos.append(number)
        else:
            Aneg.append(number)
    print(A)
    print("Positive summ", summArr(*Apos))
    print("Negative summ", summArr(*Aneg))


if __name__ == "__main__":
    main()
