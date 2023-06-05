"""
Добавить два метода в класс Dog: jump и run.
Методы выводят на экран Jump! и Run! соответственно. Создать объект и вызвать у него все методы
"""
from dog import Dog


def main():
    dog1 = Dog()
    dog1.jump()
    dog1.run()


if __name__ == "__main__":
    main()
