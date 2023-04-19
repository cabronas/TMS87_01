"""
Использовать результаты files_08. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в files_09.py.
Создать функцию подсчета полной суммы всех товаров.
Создать функцию поиска самого дорогого товара.
Создать функцию самого дешевого товара.
Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""
import csv_utils


def main():
    filecsv = "csv.csv"
    print(csv_utils.summ_counter(filecsv))
    print(csv_utils.max_price(filecsv))
    print(csv_utils.min_price(filecsv))
    n = 100
    csv_utils.decreese_count(filecsv, n)


if __name__ == "__main__":
    main()
