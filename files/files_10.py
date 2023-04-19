"""
Создать csv файл с данными следующей структуры:
Имя, Фамилия, Возраст.
Создать отчетный файл с информацией
по количеству людей входящих в ту или иную возрастную группу.
Возрастные группы:
 1-12, 13-18, 19-25, 26-40, 40+.
"""
import csv

import csv_utils

people = [
    ["Name", "Last_Name", "Age"],
    ["Vladimir", "Putirskii", 40],
    ["Vlad", "Vinichenko", 22],
    ["Nikita", "Gromov", 39]
]

cat = {
    "1-12": 0,
    "13-18": 0,
    "19-25": 0,
    "26-40": 0,
    "40+": 0
}


def main():
    filecsv = "csv_10.csv"
    filecsv_end = "csv_10_1.csv"
    csv_utils.cvs_write_full(filecsv, people)
    people2 = csv_utils.cvs_read(filecsv)
    people2 = people2[1:]
    for person in people2:
        # match person[2]:
        #     case >40:

        age = int(person[2])
        if 1 <= age <= 12:
            cat["1-12"] += 1
        if 13 <= age <= 18:
            cat["13-18"] += 1
        if 19 <= age <= 25:
            cat["19-25"] += 1
        if 26 <= age <= 40:
            cat["26-40"] += 1
        if 40 < age:
            cat["40+"] += 1
    # print(cat)
    with open(filecsv_end, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        # writer.writeheader()
        writer.writerow(cat.keys())
        writer.writerow(cat.values())


if __name__ == "__main__":
    main()
