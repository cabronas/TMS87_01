"""
Дана целочисленная квадратная матрица.
Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.
"""
import random

n = int(input("N = "))
arr = []
maxDict = {}
for i in range(n):
    column = []
    for j in range(n):
        column.append(random.randint(1, 9))
    arr.append(column)
    maxDict.update({i: [arr[i][j], 0, 0]})

# output and find max
for i in range(n):
    for j in range(n):
        print(arr[i][j], " ", end='')
        if maxDict[i][0] <= arr[i][j]:
            maxDict.update({i: [arr[i][j], i, j]})
    print()
print()

# replace
for i in range(n):
    for j in range(n):
        if i == j:
            arr[maxDict[i][1]][maxDict[i][2]], arr[i][j] = arr[i][j], maxDict[i][0]
print(*arr)
# output
for i in range(n):
    for j in range(n):
        print(arr[i][j], " ", end='')
    print()

# Спросить позже
# # replace
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             arr[maxDict[i][1]][maxDict[i][2]], arr[i][j] = arr[i][j], maxDict[i][0]
#         print(arr[i][j], " ", end='')
#     print()
# print(*arr)
