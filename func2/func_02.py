"""
Дан список слов. Сгенерировать новый список с перевернутыми словами
"""
s = ["ab", "abc", "abcd"]


def main():
    arr = [word[::-1] for word in s]
    print(arr)

if __name__ == "__main__":
    main()
