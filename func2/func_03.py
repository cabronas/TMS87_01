"""
Дан список словарей.
Каждый словарь описывает машину(серийный номер и год выпуска).
Создать новый список со всеми машинами, год выпуска которых больше n
"""
listofdict = [
    {
        "name": "Mazda",
        "serial": 123,
        "year": 2000
    },
    {
        "name": "Ford",
        "serial": 1234,
        "year": 2005
    },
    {
        "name": "Lada",
        "serial": 12345,
        "year": 2002
    }
]


def main():
    n = int(input())
    result_dict = [car for car in listofdict if car["year"] > n]
    print(*result_dict)


if __name__ == "__main__":
    main()
