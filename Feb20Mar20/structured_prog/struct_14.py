"""
Дано число. Найти сумму и произведение его цифр.
"""
summ = 0
proz = 1
numbers = input()
for number in numbers:
    summ += int(number)
    proz *= int(number)
print(summ, proz)
