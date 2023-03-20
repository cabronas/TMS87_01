"""
Создать функцию, которая принимает на вход неопределенное количество аргументов
и возвращает их сумму и максимальное из них.
"""
def summMax(*numbers):
    summ = 0
    for number in numbers:
        summ += number
    return summ, max(numbers)


summ, maxNumber = summMax(4, 3, 2, 1)
print(summ, maxNumber)