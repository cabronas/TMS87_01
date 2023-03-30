"""
Дан список имен, отфильтровать все имена, где есть буква o

[‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]
"""

name_list = ['Kate', 'Kolya', 'Alex']


def main():
    result = list(
        filter(
            lambda name: 'o' in name, name_list
        )
    )
    print(result)


if __name__ == "__main__":
    main()
