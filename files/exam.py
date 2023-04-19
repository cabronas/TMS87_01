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
    result_dict = {1: 0}
    for i in range(2, n):
        step_count = 0
        origin_count = i
        while origin_count <= i:
            if i % 2:
                i = (i * 3 + 1) // 2
                step_count += 2
            else:
                i //= 2
                step_count += 1
        result_dict[origin_count] = result_dict[i] + step_count
    result = max(result_dict, key=result_dict.get)
    return result, result_dict[result]


def main():
    n = int(input("N="))
    print(collatz(n))


if __name__ == "__main__":
    main()
