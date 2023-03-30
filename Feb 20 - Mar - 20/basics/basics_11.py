"""
Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
"""
x, y = float(input()), float(input())
avga = (x + y) / 2
print(avga)
avgg = pow(x * y, 1 / 2)
print(avgg)
