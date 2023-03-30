"""
Ввести число, проверить на то, что было введено именно число.
Возвести его в куб и вывести результат на экран.
"""


def isFloat(str):
    try:
        float(str)
        return True
    except:
        return False


s = input("Enter number: ")
a = 0
if isFloat(s):
    a = float(s) ** 3
    print(a)
else:
    print("Invalid input")
