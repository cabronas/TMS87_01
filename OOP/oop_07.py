"""
Добавить новый приватный атрибут адрес(по-умолчанию равен ‘Minsk’).
 Добавить getter и setter для адреса.
"""
from dog import Dog


def main():
    dog1 = Dog()
    print(dog1.get_address())
    dog1.set_address("Pinsk")
    print(dog1.get_address())


if __name__ == "__main__":
    main()
