"""
Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
Вычислить результат Z в зависимости от знака.
Предусмотреть реакции на возможный неверный знак операции,
а также на ввод Y=0 при делении.
Организовать возможность многократных вычислений без перезагрузки программа (т.е. построить бесконечный цикл).
В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').
"""
valid_signs = {"+", "-", "/", "*"}

while True:
    x = float(input("Enter x: "))
    sign = input("Enter sign: ")
    y = float(input("Enter y: "))
    if sign == "0":
        break
    elif sign not in valid_signs:
        print("Invalid sign")
        continue
    elif sign == "/" and y == 0:
        print("Cannot divide by 0")
        continue

    if sign == "+":
        z = x + y
    elif sign == "-":
        z = x - y
    elif sign == "*":
        z = x * y
    else:
        z = x / y
    print(z)
