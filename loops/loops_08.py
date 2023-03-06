"""
Ввести два целых числа a и b ( a < b ).
Вывести в порядке возрастания все целые числа, расположенные между a и b
(включая сами числа a и b ), а также количество n этих чисел.
"""
a = int(input("a = "))
b = int(input("b = "))
n = 0
if a > b:
    print("Invalid input")
    exit()
for c in range(a, b + 1):
    n += 1
    print(c)
print("n =", n)
