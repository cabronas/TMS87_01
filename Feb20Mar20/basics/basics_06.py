"""
Запросить у пользователя два целых числа.
Вывести строку вида “2 плюс 3 равно 5”
Примечание: после ввода переменных преобразовать переменные к типу int
 >> first_number = int(first_number)
"""
print("Enter 2 integers")
a, b = int(input()), int(input())
print(f'{a}+{b}={a + b}')
