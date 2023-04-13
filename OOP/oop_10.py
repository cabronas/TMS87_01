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
from car_10 import *


def main():
    car = Car("Ford", "Focus", 2000)
    print(car.manufacturer, car.model, car.year)
    car.print_speed()
    car.increase_speed()
    car.print_speed()
    car.decrease_speed()
    car.print_speed()
    car.decrease_speed()
    car.print_speed()
    car.reverse()
    car.print_speed()
    car.stop()
    car.print_speed()


if __name__ == "__main__":
    main()
