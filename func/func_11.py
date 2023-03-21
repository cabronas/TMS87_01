"""
Описать функцию is_power_n( k , n ) логического типа, возвращающую
True, если целый параметр k (> 0) является степенью числа n (> 1),
и False в противном случае.
Дано число n (> 1) и набор из 10 целых положительных чисел.
С помощью функции is_power_n найти количество степеней числа N в данном наборе.
"""


def is_power_n(k, n):
    if k > 0 and n > 1:
        if k == 1:
            return True
        power = 1
        while (power < n):
            power = power * k
        if power == n:
            return True
    return False


n1 = 101
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    for number in arr:
        if is_power_n(number, n1):
            print(number)


if __name__ == "__main__":
    main()
