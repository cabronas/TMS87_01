"""
Описать функцию fact2( n ),
вычисляющую двойной факториал
:n!! = 1·3·5·...·n, если n — нечетное;
n!! = 2·4·6·...·n, если n — четное.
С помощью этой функции найти двойные факториалы пяти данных целых чисел
"""


def fact2(n):
    result = 1
    if n < 0:
        return None
    if n % 2 == 0:
        i = 2
        while i <= n:
            result *= i
            i += 2
    else:
        i = 1
        while i <= n:
            result *= i
            i += 2
    return result


def main():
    print("Введите 5 чисел через пробел:")
    arr = input().split(" ")
    for number in arr:
        print(f"{number}: {fact2(int(number))}")


if __name__ == "__main__":
    main()
