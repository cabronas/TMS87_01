"""
Создать скрипт, который при з
апуске принимает неопределенное количество аргументов и считает сумму тех из них, что являются цифрами.
Пример:
python test.py 1 2 3 4 a b 5 6 -->  21

"""
import sys
args = sys.argv
ints = sum(map(int, filter(lambda x: x.isdigit(), args)))
print(ints)
