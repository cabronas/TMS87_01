"""
Для каждого натурального числа в промежутке от m до n вывести все делители, кроме единицы и самого числа. m и n вводятся с клавиатуры.
Пример:
m =100, n = 105
100: 2 4 5 10 20 25 50
101:
102: 2 3 6 17 34 51
103:
104: 2 4 8 13 26 52
105: 3 5 7 15 21 35
"""


def findDividers(number):
    arr = []
    for i in range(2, number):
        if number % i == 0:
            arr.append(i)
    return arr


m = int(input("M = "))
n = int(input("N = "))
for i in range(m, n+1):
    print(str(i)+":", *findDividers(int(i)))
