"""
Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
"""


def summArr(*numbers):
    summ = 0
    for index, number in enumerate(numbers):
        summ += number * index
    return summ


def main():
    print(summArr(4, 3, 2, 1))


if __name__ == "__main__":
    main()
