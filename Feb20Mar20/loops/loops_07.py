"""
Получить сумму кубов натуральных чисел от n до m, используя цикл for
"""
n = int(input("Enter n: "))
m = int(input("Enter m: "))
summ = 0
for n in range(n, m+1):
    summ += n ** 3
print(summ)
