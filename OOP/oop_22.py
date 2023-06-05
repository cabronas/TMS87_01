"""
Сделать атрибут counter приватным.
Создать метод класса get_counter.
Создать три объекта класса. Вызвать через класс метод get_counter.
"""
from animals import Pet


def main():
    pet1 = Pet("Barsik", 4, "Maxim", 10, 10)
    pet2 = Pet("Sharsik", 4, "Maxim", 10, 10)
    pet3 = Pet("Barsik2", 4, "Maxim", 10, 10)
    print(Pet.get_counter())


if __name__ == "__main__":
    main()
