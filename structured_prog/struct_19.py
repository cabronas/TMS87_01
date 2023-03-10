"""
Дана целочисленная квадратная матрица.
Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.
"""
n = int(input("N = "))
arr = []
maxDict = {}
for i in range(n):
    column = []
    for j in range(n):
        column.append(int(input()))
    arr.append(column)
    maxDict.update({i: arr[i][0]})

# output and find max
for i in range(n):
    for j in range(n):
        print(arr[i][j], " ", end='')

        if maxDict[i] < arr[i][j]:
            maxDict.update({i: arr[i][j]})
    print()
print()

# replace
for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = maxDict[i]
        print(arr[i][j], " ", end='')
    print()
