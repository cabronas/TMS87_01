"""
Дан список целых чисел. Подсчитать сколько четных чисел в списке
"""
a = input().split()
counter = 0
for number in a:
    if int(number) % 2 == 0:
        counter += 1
print(counter)
