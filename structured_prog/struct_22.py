"""
Создать список поездов.
Структура словаря:
номер поезда,
пункт прибытия
время прибытия,
пункт отбытия
время отбытия.

Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
Примечание: данное задание подразумевает самостоятельное изучение принципов работы со временем в Python(библиотека datetime)
"""
import datetime
import time

t = datetime.datetime.today()
trains = [
    {
        "Number": "00",
        "toP": "Minsk",
        "toTime": datetime.datetime(2022, 2, 2, 15, 0),
        "fromP": "Moscow",
        "fromTime": datetime.datetime(2022, 2, 2, 22, 0)
    }
    ,
    {
        "Number": "01",
        "toP": "Moscow",
        "toTime": datetime.datetime(2022, 2, 2, 15, 0),
        "fromP": "Khabarovsk",
        "fromTime": datetime.datetime(2022, 2, 3, 15, 0)
    }
]
print(trains[0]["toTime"])
for train in trains:
    travelTime = (train["fromTime"] - train["toTime"]).total_seconds() / 60.0  # Minutes
    if travelTime > 440:
        print(*train.values())
