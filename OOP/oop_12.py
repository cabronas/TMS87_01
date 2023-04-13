"""
Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
Унаследовать Dog, Cat, Parrot от класса Pet.
Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
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
