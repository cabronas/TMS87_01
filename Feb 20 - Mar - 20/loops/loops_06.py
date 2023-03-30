"""
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор,
пока не выпадет 7.
"""
import random

while True:
    randint = random.randint(1, 10)
    print(randint)
    if randint == 7:
        break
