"""
Задан целочисленный массив.
Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).
"""
s = input().split(" ")
arr = []
for i in range(len(s)):
    arr.append(int(s[i]))
segmentCount = 0
segmentFlag = False
for i in range(len(arr)):
    if arr[i - 1] < arr[i]:
        if not segmentFlag:
            segmentFlag = True
            segmentCount += 1
    else:
        segmentFlag = False
print(segmentCount)
