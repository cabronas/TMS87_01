"""
Создать файл animals.py.
Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump,
birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод
fly. Cat - meow, Dog - bark.
"""
from animals import *


def main():
    dog = Dog("Barsik", 4, "Maxim")
    print(dog.name, dog.age, dog.master)
    dog.jump(3)
    dog.bark()
    dog.run(3)
    print()
    cat = Cat("Sharik", 3, "Maxim")
    print(cat.name, cat.age, cat.master)
    cat.jump(3)
    cat.meow()
    cat.run(3)
    print()
    parrot = Parrot("Pat", 2, "Maxim")
    print(parrot.name, parrot.age, parrot.master)
    parrot.jump(3)
    parrot.fly(2)
    parrot.run(3)


if __name__ == "__main__":
    main()
