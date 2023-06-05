"""
Добавить в класс Pet пустой метод voice.
 Заменить имена методов bark, meow на voice. Добавить voice для класса Parrot.
Создать функцию, принимающую список животных и вызывающую у каждого животного метод voice.
"""
from animals import *


def main():
    dog = Dog("Barsik", 4, "Maxim", 10, 10)
    print(dog.name, dog.age, dog.master, dog.weight, dog.height)
    dog.voice()
    print()
    cat = Cat("Sharik", 3, "Maxim", 5, 5)
    print(cat.name, cat.age, cat.master, cat.weight, cat.height)
    cat.voice()
    print()
    parrot = Parrot("Pat", 2, "Maxim", 3, 3, "Grey parrot")
    print(parrot.name, parrot.age, parrot.master, parrot.weight, parrot.height)
    parrot.voice()


if __name__ == "__main__":
    main()
