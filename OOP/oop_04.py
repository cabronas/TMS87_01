"""
Создать класс Dog.
Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран.
Создать объект класса Dog,
вызвать все методы объекта и вывести на экран все его атрибуты.
"""

from dog import Dog


def main():
    dog1 = Dog("Barsik", 40, 30, 10)
    dog1.bark()
    dog1.run()
    dog1.jump()
    print(dog1.name, dog1.height, dog1.weight, dog1.age)


if __name__ == "__main__":
    main()
