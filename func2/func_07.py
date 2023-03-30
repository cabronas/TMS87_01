# """
# Дан список чисел. Найти произведение всех чисел, которые кратны 3.
# """
from functools import reduce

list_int = [1, 3, 6, 10, 11, 3]


def main():
    # result3 = filter(
    #     lambda x: x % 3 == 0, list_int
    # )
    # result = reduce(
    #     lambda a, x: x * a, result3, 1
    # )
    result = reduce(
        lambda a, x: x * a,
        filter(lambda x: x % 3 == 0, list_int), 1
    )
    print(result)


if __name__ == "__main__":
    main()
