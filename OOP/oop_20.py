"""
Создать файл time1.py.
Создать класс MyTime.
Атрибуты: hours, minutes, seconds.
Переопределить магические методы сравнения(равно, не равно),
сложения, вычитания, вывод на экран.
"""
from time1 import MyTime


def main():
    time1 = MyTime(10, 30, 55)
    time2 = MyTime(10, 40, 55)
    print(time1)
    print(time2)
    time3 = time1 + time2
    print(time3)
    time3 = time3 - time2
    print(time3)
    print(time1 == time3)
    print(time3 != time2)

    time4 = MyTime(time2)
    print(time4)
    time4 = MyTime("1-2-3")
    print(time4)


if __name__ == "__main__":
    main()
