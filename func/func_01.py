"""
Написать функцию, которая получает на вход имя и выводит строку вида:
 “Hello, {name}”. Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""


def hello(s):
    print(f"Hello {s}")


names = ["a", "b", "c", "d", "e"]


def main():
    for name in names:
        hello(name)


if __name__ == "__main__":
    main()
