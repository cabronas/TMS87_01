"""
Создать универсальный декоратор,
который меняет порядок аргументов в функции на противоположный.
"""


def decorator_reverse(func):
    def wrapper(*args):
        reverse_arg_list = list(args)
        reverse_arg_list.reverse()
        result = func(*reverse_arg_list)
        return result

    return wrapper

@decorator_reverse
def test_func(a, b):
    print(a)
    print(b)
    return


def main():
    a = "a"
    b = "b"
    print(test_func(a, b))


if __name__ == "__main__":
    main()
