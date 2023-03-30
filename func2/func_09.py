"""
Дан список строк.
Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке. Использовать генератор списков.
"""
from functools import reduce

arr_of_strings = [
    "a", "ab", "abc"
]


def main():
    new_arr = [f"{index} - {word}" for index, word in enumerate(arr_of_strings)]
    print(new_arr)


if __name__ == "__main__":
    main()
