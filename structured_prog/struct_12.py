"""
Составить список чисел Фибоначчи содержащий 15 элементов.

(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле.

"""
f0 = 0
f1 = 1
febNumberArr = []
# Fn = F n-1 + F n-2 (applies to all other integers)
febNumberArr.append(f1)
for i in range(1, 15):
    febNumber = f0 + f1
    f0 = f1
    f1 = febNumber
    febNumberArr.append(febNumber)
print()
print(*febNumberArr)

i = 1
f0 = 0
f1 = 1
febNumberArr = []
febNumberArr.append(f1)
while i != 15:
    febNumber = f0 + f1
    f0 = f1
    f1 = febNumber
    i += 1
    febNumberArr.append(febNumber)
print(*febNumberArr)
