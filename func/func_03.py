"""
Написать программу для нахождения факториала.
Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно
"""


def factorial(n):
    fact = 0
    for i in range(0, n + 1):
        fact += i
    return fact


numbers = int(input("N="))
print(factorial(numbers))
