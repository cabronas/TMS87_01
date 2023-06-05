"""
Добавить в класс Pet атрибут counter = 0,
значение которого увеличивается при создании любого объекта.
"""
from animals import Pet


def main():
    pet1 = Pet("Barsik", 4, "Maxim", 10, 10)
    pet2 = Pet("Barsik", 4, "Maxim", 10, 10)
    print(Pet.counter)


if __name__ == "__main__":
    main()
