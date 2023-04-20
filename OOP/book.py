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
import string


class BookTypeException(Exception):
    def __init__(self, message="Incorrect input type"):
        super().__init__(message)


class PageCountException(Exception):
    def __init__(self, message="Incorrect page count"):
        super().__init__(message)


class PriceException(Exception):
    def __init__(self, message="Incorrect price"):
        super().__init__(message)


class Book:
    def __init__(self, name, page_count, year_of_release, author, price):
        if not ((name.__class__ == str) and
                (page_count.__class__ == int) and
                (year_of_release.__class__ == int) and
                (author.__class__ == str) and
                (price.__class__ == int or price.__class__ == float)):
            raise BookTypeException()
        else:
            if page_count <= 0:
                raise PageCountException()
            elif price <= 0:
                raise PriceException()
        self.__name = name
        self.__page_count = page_count
        self.__year_of_release = year_of_release
        self.__author = author
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, page_count):
        self.__page_count = page_count

    @property
    def year_of_release(self):
        return self.__year_of_release

    @year_of_release.setter
    def year_of_release(self, year_of_release):
        self.__year_of_release = year_of_release

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @classmethod
    def get_counter(cls):
        pass
