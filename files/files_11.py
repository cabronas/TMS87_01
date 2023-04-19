"""
Создать csv файл с данными о ежедневной погоде.
Структура:  Дата, Место, Градусы, Скорость ветра.
Найти среднюю погоду(скорость ветра и градусы)
для Минск за последние 7 дней.
"""
import csv

import csv_utils

weather = [
    ["Date", "Place", "Temperature", "Wind speed"],
    ["01.05", "Minsk", "10", "2"],
    ["02.05", "Minsk", "11", "3"],
    ["03.05", "Minsk", "9", "4"],
    ["04.05", "Minsk", "3", "2"],
    ["05.05", "Minsk", "15", "1"],
    ["06.05", "Minsk", "11", "3"],
    ["07.05", "Minsk", "13", "4"],
    ["07.05", "Grodno", "1", "1"]
]


def main():
    filecsv = "csv_10.csv"
    csv_utils.cvs_write_full(filecsv, weather)
    # weather1 = csv_utils.cvs_read(filecsv)[1:].reverse()
    weather1 = csv_utils.cvs_read(filecsv)[1:]
    weather1.reverse()
    days_counted = 0
    avgTemp = 0
    avgWind = 0
    for day in weather1:
        if day[1] == "Minsk":
            avgTemp += int(day[2])
            avgWind += int(day[3])
            days_counted += 1
        if days_counted == 7:
            break
    avgTemp = round(avgTemp / days_counted, 2)
    avgWind = round(avgWind / days_counted, 2)
    weather1.reverse()
    weather1.append(["Average weather", avgTemp, avgWind])
    csv_utils.cvs_write_full(filecsv, weather1)


if __name__ == "__main__":
    main()
