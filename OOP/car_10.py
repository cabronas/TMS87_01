"""
Создать файл car10.py. Создать класс Car.
Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5),
уменьшение скорости(скорость  - 5),
стоп(сброс скорости на 0),
отображение скорости,
разворот(изменение знака скорости).
Все атрибуты приватные.
"""


class Car:
    def __init__(self, manufacturer, model, year, speed=0):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def print_speed(self):
        print(f"Current speed: {self.speed}")

    def reverse(self):
        self.speed *= -1
