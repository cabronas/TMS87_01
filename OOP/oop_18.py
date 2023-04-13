"""
Унаследовать от класса Pet два класса: Horse, Donkey. Переопределить в классах методы voice.
Создать класс Mule. Класс Mule должен наследоваться от классов Horse и Donkey.
Метод voice должен быть унаследован от класса Donkey
"""

from animals import *


def main():
    mule = Mule("Sharik", 3, "Maxim", 5, 5)
    mule.voice()


if __name__ == "__main__":
    main()