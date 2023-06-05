"""
Сделать все атрибуты класса Dog приватными.
Сделать для каждого атрибута getter и setter используя декораторы.
Все change методы удалить
"""
from dog import Dog


def main():
    dog1 = Dog()
    dog1.height = 30
    print(dog1.height)


if __name__ == "__main__":
    main()
