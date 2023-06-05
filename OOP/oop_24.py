"""
Создать файл book.py. Создать класс Book.
Атрибуты:
количество страниц,
год издания,
автор,
цена.
Добавить валидацию в конструкторе на ввод корректных данных.
Создать иерархию ошибок.
 Ошибки вызываются при попытке создания неправильного объекта.
 Обработка происходит в пользовательском коде(в main).
"""

from book import Book
from book import BookTypeException, PageCountException, PriceException


def main():
    name = "Преступление и наказание1"
    page_count = 200
    year = 1865
    author = "Фёдор Достоевский"
    price = -2000
    correct = None
    try:
        print(name, page_count, year, author, price)
        correct = Book(name, page_count, year, author, price)
        print(correct.name)
    except BookTypeException:
        print("Incorrect input type")
        print("No action will be taken")
    except PageCountException:
        print("Incorrect page count")
        print("Reseting page count to 1")
        page_count = 1
        correct = Book(name, page_count, year, author, price)
    except PriceException:
        print("Incorrect price")
        print("Reseting price to 1")
        price = 1
        correct = Book(name, page_count, year, author, price)
    finally:
        if correct is not None:
            print(correct.name, correct.page_count, correct.author, correct.price, correct.year_of_release)


if __name__ == "__main__":
    main()
