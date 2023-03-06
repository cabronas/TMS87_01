"""
Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
Найти сумму всех элементов матрицы, которые кратны 3.
"""
import random

n = int(input("n = "))
arr = []
for i in range(n):
    Column = []
    for j in range(n):
        Column.append(random.randint(1, 9))
    arr.append(Column)

summ = 0
for i in range(n):
    for j in range(n):
        print(arr[i][j], " ", end='')
        if arr[i][j] % 3 == 0:
            summ += arr[i][j]
    print()
print(summ)
