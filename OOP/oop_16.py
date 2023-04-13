"""Добавить в класс Parrot  новый атрибут - species"""
from animals import *


def main():
    parrot = Parrot("Pat", 2, "Maxim", 3, 3, "Grey parrot")
    print(parrot.name, parrot.age, parrot.master, parrot.weight, parrot.height, parrot.species)
    parrot.jump(3)


if __name__ == "__main__":
    main()
