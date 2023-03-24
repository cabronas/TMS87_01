"""
Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива.
"""
import random

n = int(input("n = "))
m = int(input("m = "))
arr = []
for i in range(n):
    Column = []
    for j in range(m):
        Column.append(random.randint(1, 9))
    arr.append(Column)

count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], " ", end='')
        if arr[i][j] == 7:
            count += 1
    print()
print(count)
