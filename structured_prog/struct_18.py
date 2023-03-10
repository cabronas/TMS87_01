"""
Задан целочисленный массив.
Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).
"""
s = input().split(" ")
arr = []
for i in range(len(s)):
    arr.append(int(s[i]))

longestSegment = []
segment = []
for i in range(len(arr)):
    if arr[i - 1] < arr[i]:
        segment.append(arr[i])
        if len(segment) > len(longestSegment):
            longestSegment = segment
    else:
        if len(segment) > len(longestSegment):
            longestSegment = segment
        segment = [arr[i]]
print(longestSegment)
