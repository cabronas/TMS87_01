"""
Написать функцию принимающая на вход неопределенным количеством аргументов
и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
Написать программу в виде трех функций.
"""


def sredAr(*numbers: int):
    sredA = 0
    for number in numbers:
        sredA += number
    return sredA / len(numbers)


def sredGe(*numbers: int):
    sredG = 1
    for number in numbers:
        if number < 0: return None
        sredG *= number
    return pow(sredG, 1 / len(numbers))


def sred(*numbers, mean_type):
    if mean_type == 1:
        return sredAr(*numbers)
    elif mean_type == 2:
        return sredGe(*numbers)


def main():
    print(sred(1, 2, 3, 4, mean_type=1))
    print(sred(1, 2, 3, 4, mean_type=2))


if __name__ == "__main__":
    main()
