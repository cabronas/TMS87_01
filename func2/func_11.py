"""
Создать декоратор для функции,
которая принимает список чисел.
Декоратор должен производить предварительную проверку данных
- удалять все четные элементы из списка.
"""


def decorator_remove_even(func):
    def wrapper(arr: list):
        for number in arr:
            if number % 2 == 0:
                arr.remove(number)
        result = func(arr)
        print(result)
        return result
    return wrapper


@decorator_remove_even
def reverseArr(arr: list):
    return arr[::-1]


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reverseArr(a)


if __name__ == "__main__":
    main()
