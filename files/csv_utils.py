"""
Написать функции по работе с csv файлами в файле csv_utils.py.
Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
Удаление записи(по позиции, по-умолчанию последнюю).
В файле files_08 импортировать функции.
С помощью функций создать файл с информацией о товарах(Имя товара, цена, количество, комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""
import csv


def cvs_read(file_name):
    table = []
    with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            table.append(row)
    return table


def cvs_write_full(file_name, table):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerows(table)


def cvs_writer(file_name, row, pos=False):
    table = cvs_read(file_name)
    if pos != False:
        table.insert(pos, row)
    else:
        table.append(row)
    cvs_write_full(file_name, table)


def cvs_deleter(file_name, pos=False):
    table = cvs_read(file_name)
    if pos != False:
        table.pop(pos + 1)
    else:
        table.pop()
    cvs_write_full(file_name, table)


def summ_counter(file_name):
    table = cvs_read(file_name)
    p = 0
    i = 1
    while i < len(table):
        p += int(table[i][1])
        i += 1
    return p


def max_price(file_name):
    table = cvs_read(file_name)
    max = int(table[1][1])
    i = 1
    while i < len(table):
        value = int(table[i][1])
        max = max if max > value else value
        i += 1
    return max


def min_price(file_name):
    table = cvs_read(file_name)
    min = int(table[1][1])
    i = 1
    while i < len(table):
        value = int(table[i][1])
        min = min if min < value else value
        i += 1
    return min


def decreese_count(file_name, n=1):
    table = cvs_read(file_name)
    i = 1
    while i < len(table):
        table[i][2] = int(table[i][2]) - n
        i += 1
    cvs_write_full(file_name, table)
