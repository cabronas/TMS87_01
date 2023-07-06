"""
Создать бесконечный генератор случайных чисел.
Использовать в генераторе временную задержку
from time import sleep
"""
import random
import time


def number_gen():
    time.sleep(1)
    while True:  # ???
        yield random.randint(1, 10)


def main():
    rng = number_gen()
    for i in range(3):
        print(next(rng))


if __name__ == "__main__":
    main()
