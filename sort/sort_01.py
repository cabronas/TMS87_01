# bubble
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
swap = 0
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            swap = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = swap
print(*arr)

# insert
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
for i in range(len(arr)):
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        swap = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = swap
        j -= 1
print(*arr)
