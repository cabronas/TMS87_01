"""
Создать lambda функцию,
которая принимает на вход неопределенное количество именованных аргументов
и выводит словарь с ключами удвоенной длины.
{‘abc’: 5} -> {‘abcabc’: 5}
"""
from functools import reduce


def main():
    result = (lambda **kwargs: {k * 2: v for k, v in kwargs.items()})(a=1, b=2)
    print(result)


if __name__ == "__main__":
    main()
