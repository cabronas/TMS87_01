"""
Дан список чисел. Посчитать сколько раз встречается каждое число.
Использовать функцию.
Подсказка: для хранения данных использовать словарь.
Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in
"""

arr = [1, 2, 3, 1, 1, 2, 5, 5, 5, 5]


def getOcc(array):
    numberDict = {}
    for index, number in enumerate(array):
        if number not in numberDict:
            numberDict.update({number: 1})
        else:
            numberDict.update(
                {
                    number: numberDict[number] + 1
                }
            )
    print(numberDict)
    return numberDict


def main():
    getOcc(arr)


if __name__ == "__main__":
    main()
