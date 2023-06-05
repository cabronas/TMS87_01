"""
Добавить метод jump, принимающий высоту прыжка. Метод выводит сообщение “Jump X meters”
Переопределить метод jump в дочерних классах. Если передать методу jump класса dog значение больше 0.5,
выводить сообщение “Dogs cannot jump so high, аналогично для кошек(2), для попугаев(0.05)
"""

from animals import *


def main():
    dog = Dog("Barsik", 4, "Maxim", 10, 10)
    print(dog.name, dog.age, dog.master, dog.weight, dog.height)
    dog.jump(10)
    print()
    cat = Cat("Sharik", 3, "Maxim", 5, 5)
    print(cat.name, cat.age, cat.master, cat.weight, cat.height)
    cat.jump(1)
    print()
    parrot = Parrot("Pat", 2, "Maxim", 3, 3)
    print(parrot.name, parrot.age, parrot.master, parrot.weight, parrot.height)
    parrot.jump(3)


if __name__ == "__main__":
    main()
