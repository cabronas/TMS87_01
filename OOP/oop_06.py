"""
Добавить в метод инициализации новый приватный атрибут - master.
 Создать метод get_master()
 который возвращает значение атрибута master.
"""
from dog import Dog

def main():
    dog1 = Dog("Barsik", 40, 30, 10, "Maxim")
    print(dog1.get_master())


if __name__ == "__main__":
    main()
