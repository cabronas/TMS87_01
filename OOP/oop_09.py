"""
Создать файл classes09.py.
Создать пять!!! :( классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута,
конструктор, геттеры и сеттеры для каждого атрибута, два метода.
"""
from classes_09 import *


def main():
    dinosaur = Dinosaur()
    print(dinosaur.name)
    dinosaur.grow(5)
    dinosaur.jump(3)
    print()
    crow = Bird()
    print(crow.name)
    crow.fly(5)
    crow.grow(5)
    print()
    car = Car()
    print(car.name)
    car.drive(100)
    car.change_name("GT")
    print()
    student = Student()
    print(student.clas, student.name, student.average_grade)
    student.change_clas("9")
    student.increase_grade()
    print(student.clas, student.name, student.average_grade)
    print()
    laptop = Laptop()
    print(laptop.name, laptop.processor, laptop.manufacturer)
    laptop.change_processor("10750h")
    laptop.change_manufacturer("MSI")
    print(laptop.name, laptop.processor, laptop.manufacturer)


if __name__ == "__main__":
    main()
