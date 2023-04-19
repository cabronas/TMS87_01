"""
Написать функции по работе с csv файлами в файле csv_utils.py.
Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
Удаление записи(по позиции, по-умолчанию последнюю).
В файле files_08 импортировать функции.
С помощью функций создать файл с информацией о товарах(Имя товара, цена, количество, комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""
import csv_utils


def main():
    tovarList = [
        ["name", "price", "count", "commentary"],
        ["apple", "3", "3000", "a?"],
        ["orange", "10", "4000", "b?"],
        ["potato", "2", "200", "c?"]
    ]
    tovar = ["bananas", "5", "2002", "d?"]
    csv_utils.cvs_write_full("csv.csv", tovarList)
    csv_utils.cvs_writer("csv.csv", tovar)
    csv_utils.cvs_deleter("csv.csv", 2)


if __name__ == "__main__":
    main()
