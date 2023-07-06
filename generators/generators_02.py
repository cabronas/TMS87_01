"""
Создать бесконечный генератор случайных чисел. Генератор должен принимать диапазон случайных чисел и смещение
Пример: a = 1, b = 10, diff = 10
1- 10
11-20
…
N +10 - M + 10
"""
import random
import time


def number_gen(a=1, b=10, diff=10):
    time.sleep(1)
    while True:  # ???
        yield random.randint(a, b)
        a += diff
        b += diff


def main():
    rng = number_gen(3, 30, 5)
    for i in range(3):
        print(next(rng))


if __name__ == "__main__":
    main()
