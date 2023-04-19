"""
Дан файл, содержащий различные даты.
Каждая дата - это число, месяц и год.
Найти самую раннюю дату.
"""
import csv

import csv_utils
import datetime

days = [
    ["Date"],
    ["01/05/2012"],
    ["02/04/2023"],
    ["03/01/2026"],
    ["11/10/2013"],
]


def main():
    filecsv = "csv_10.csv"
    csv_utils.cvs_write_full(filecsv, days)
    days1 = csv_utils.cvs_read(filecsv)[1:]
    earliest_date = datetime.datetime.strptime(*days1[0], '%d/%m/%Y')
    for day in days1:
        converted_day = datetime.datetime.strptime(*day, '%d/%m/%Y')
        if converted_day < earliest_date:
            earliest_date = converted_day
    print(earliest_date.date())


if __name__ == "__main__":
    main()
