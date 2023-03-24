"""
Создать lambda функцию,
которая принимает на вход неопределенное количество именованных аргументов
и выводит словарь с ключами удвоенной длины.
{‘abc’: 5} -> {‘abcabc’: 5}
"""
from functools import reduce


def main():
    args = ("abc", "abcabc")
    result = (
        lambda *x:
        {value*2: "5" for value in x})(*args)
    print(result)


if __name__ == "__main__":
    main()
