"""
Добавить в класс Dog метод change_name.
Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""
from dog import Dog


def main():
    dog1 = Dog("Barsik", 40, 30, 10)
    print(dog1.name)
    dog1.change_name("Sharik")
    print(dog1.name)


if __name__ == "__main__":
    main()
