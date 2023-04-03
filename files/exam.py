"""
Напишите функцию collatz с одним аргументом n. Функция должна возвращать
2-элементный кортеж:
– первый элемент – число k (1 ≤ k < n) такое, что у него самая длинная траектория
среди всех чисел в диапазоне [1, n);
– второй элемент – длина его траектории.
f(n) = {
n/2, n чётное;
3n + 1, иначе
}
"""


def formula(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def collatz(n):
    max_collatz = [1, 0]
    for i in range(1, n + 1):
        length = 0
        curent_value = i
        while curent_value != 1:
            length += 1
            curent_value = formula(curent_value)
        if max_collatz[1] < length:
            max_collatz = [i, length]
    return tuple(max_collatz)


def main():
    n = int(input("N="))
    print(collatz(n))


if __name__ == "__main__":
    main()
