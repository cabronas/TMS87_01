"""
Дан список чисел. Вернуть список, где каждое число переведено в строку
[5, 3] -> [‘5’, ‘3’]
"""
arr_of_int = [1, 2, 3, 4, 5, 6]


def main():
    result = [str(number) for number in arr_of_int]
    print(result)
    result = list(
        map(
            lambda x: str(x), arr_of_int
        )
    )
    print(result)


if __name__ == "__main__":
    main()
