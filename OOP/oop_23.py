"""
Создать статичный метод get_random_name для класса Pet.
Метод возвращает случайную строку вида A-42.
"""

from animals import Pet


def main():
    print(Pet.get_random_name())
    print(Pet.get_random_name())
    print(Pet.get_random_name())


if __name__ == "__main__":
    main()
