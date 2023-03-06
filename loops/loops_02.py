"""
Дан произвольный список, содержащий только числа.
Выведите результат сложения всех чисел больше 10.
"""
my_list = input().split(' ')
summ = 0
for number in my_list:
    if int(number) > 10:
        summ += int(number)
print(summ)
