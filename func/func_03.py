"""
Написать программу для нахождения факториала.
Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно
"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def main():
    numbers = int(input("N="))
    print(factorial(numbers))


if __name__ == "__main__":
    main()
