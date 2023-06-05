"""
Два натуральных числа называют дружественными,
если каждое из них равно сумме всех делителей другого, кроме самого этого числа.
Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300.
"""


def findDividersSum(number):
    summ = 0
    for i in range(1, number):
        if number % i == 0:
            summ += i
    return summ


for i in range(200, 301):
    j = findDividersSum(i)
    if findDividersSum(j) == i and i < j:
        print(i, j)
