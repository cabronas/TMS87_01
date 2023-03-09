"""
Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.
"""
import random

n = int(input("n = "))
arr = []
for i in range(n):
    Column = []
    for j in range(n):
        Column.append(random.randint(1, 9))
    arr.append(Column)

for i in range(n):
    for j in range(n):
        print(arr[i][j], " ", end='')
    print()
