"""
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 ->  2 3 4 5 1
предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.
"""
arr = input().split(" ")
buffer = 0
# for
for index, value in enumerate(arr):
    if index == 0:
        buffer = value
        arr[index] = arr[index + 1]
    elif index == len(arr) - 1:
        arr[index] = buffer
    else:
        arr[index] = arr[index + 1]
print(arr)

# while
counter = 0
while counter != len(arr):
    if counter == 0:
        buffer = arr[counter]
        arr[counter] = arr[counter + 1]
    elif counter == len(arr) - 1:
        arr[counter] = buffer
    else:
        arr[counter] = arr[counter + 1]
    counter += 1
print(arr)
