"""
Создать функцию,
которая принимает на вход неопределенное количество именованных аргументов и
выводит на экран те из них, длина ключа которых четна.
"""


def evenKey(**dict):
    dreturn = {}
    for key, value in dict.items():
        if len(key) % 2 == 0:
            print(key, value)
            dreturn[key] = value
    return dreturn


def main():
    evenKey(a=1, ab=2, abc=3, abcd=4)


if __name__ == "__main__":
    main()
