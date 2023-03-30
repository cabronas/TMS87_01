"""
Создать lambda функцию,
которая принимает на вход имя и выводит его в формате “Hello, {name}”
"""


def main():
    s = input()
    result = (lambda x: "Hello " + x)(s)
    print(result)


if __name__ == "__main__":
    main()
