"""
Получить на ввод количество рублей и копеек       #Вместе?
и вывести в правильной форме, например,
3 рубля, 1 рубль 25 копеек, 3 копейки
"""
a = input()
if "," not in a:
    a += ", "
ruble, cents = a.split(",")
result = ""

# Рубли
if ruble == "":
    result += "0 рублей"
elif ruble[-1] == "0":
    result += ruble + " рублей"
elif ruble[-1] == "1":
    result += ruble + " рубль"
else:
    result += ruble + " рубля"

# Копейки
if cents == "0" or cents == "":
    pass
elif cents[-1] == "1":
    result += ", " + cents + " копейка"
elif cents[-1] in ["2", "3", "4"]:
    result += ", " + cents + " копейки"
else:
    result += ", " + cents + " копеек"

print(result)
