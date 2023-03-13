"""
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им все четные по значению элементы.
"""
import random

arr = []
maxN = 0
for i in range(19):
    arr.append(random.randint(1, 21))
    if i != 0:
        if arr[i] > maxN:
            maxN = arr[i]
    else:
        maxN = arr[i]
print(arr)
print("max =", maxN)

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = maxN
print(arr)
