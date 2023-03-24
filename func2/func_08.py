"""
Написать декоратор, который будет выводить время выполнения функции
from datetime import datetime
time = datetime.now()

"""
import time
from datetime import datetime


def time_decorator(func):
    def wrapper(n):
        time_start = datetime.now()
        result = func(n)
        time_end = datetime.now()
        print((time_end - time_start).microseconds / 1000)  # milliseconds
        print(result)
        return result

    return wrapper


@time_decorator
def mul(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        # time.sleep(1)
    return result


def main():
    mul(5)


if __name__ == "__main__":
    main()
