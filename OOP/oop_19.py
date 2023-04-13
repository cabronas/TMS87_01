"""
Определить магические методы сравнения для класса Pet:
на равенство и неравенство. Два животных равны тогда,
когда равны их возрасты, их рост и вес и класс.
"""

from animals import *


def main():
    dog = Dog("Barsik", 4, "Maxim", 10, 10)
    print(dog.name, dog.age, dog.master, dog.weight, dog.height)
    cat = Cat("Sharik", 3, "Maxim", 5, 5)
    print(cat.name, cat.age, cat.master, cat.weight, cat.height)
    parrot = Parrot("Pat", 2, "Maxim", 3, 3, "Grey parrot")


if __name__ == "__main__":
    main()