"""
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы,
превосходящих среднее арифметическое значение элементов матрицы и
сумма индексов которых четна.
"""
import random

# init
n = int(input("n = "))
m = int(input("m = "))
A = []
for i in range(n):
    Column = []
    for j in range(m):
        Column.append(random.randint(1, 9))
    A.append(Column)

# average calculation
count = 0
average = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], " ", end='')
        average += A[i][j]
        count += 1
    print()
average = average / count
print("average = ", average)
# count
count = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if ((A[i][j] > average) and ((i + j) % 2 == 0)):
            count += 1
print(count)
