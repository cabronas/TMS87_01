"""
Дан словарь, создать новый словарь, поменяв местам ключ и значение
"""

testdict =\
    {
    "abc": "1",
    "dda": "2",
    "caa": "3"
    }


def main():
    result = {value: key for key, value in testdict.items()}
    print(result)


if __name__ == "__main__":
    main()
