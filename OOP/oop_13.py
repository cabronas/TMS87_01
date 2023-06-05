"""
Добавить два новых атрибута в родительский класс: weight и height.
Добавить методы change_weight, change_height принимающий один параметр
и прибавляющий его к соответствующему аргументу.
В случае если параметр не был передан, увеличивать на 0.2.
Изменить метод fly класса Parrot.
Если вес больше 0.1 выводить сообщение This parrot cannot fly.
"""
from animals import *


def main():
    dog = Dog("Barsik", 4, "Maxim", 10, 10)
    print(dog.name, dog.age, dog.master, dog.weight, dog.height)
    dog.jump(3)
    dog.bark()
    dog.run(3)
    dog.change_weight(3)
    print(dog.name, dog.age, dog.master, dog.weight, dog.height)
    print()
    cat = Cat("Sharik", 3, "Maxim", 5, 5)
    print(cat.name, cat.age, cat.master, cat.weight, cat.height)
    cat.jump(3)
    cat.meow()
    cat.run(3)
    cat.change_height(-2)
    print(cat.name, cat.age, cat.master, cat.weight, cat.height)
    print()
    parrot = Parrot("Pat", 2, "Maxim", 3, 3)
    print(parrot.name, parrot.age, parrot.master, parrot.weight, parrot.height)
    parrot.jump(3)
    parrot.fly(2)
    parrot.run(3)


if __name__ == "__main__":
    main()
