"""
Написать игру. Пользователь должен угадать число.
Сперва вводится диапазон угадывания. После колличество попыток.
В случае правильного ответа - выводить You are the winner.
В случае неправильного давать игроку подсказку(больше или меньше искомое число).
Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.
"""
import random

# correct = random.randint(1, 100)
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
correct = random.randint(lower, upper)
tries = int(input("Enter amount of tries: "))
while True:
    guess = int(input())
    if guess == correct:
        print("You are the winner")
        break
    elif guess < correct:
        print("You guess is less then the value")
    elif guess > correct:
        print("You guess is more then the value")
    tries -= 1
    if tries == 0:
        print("You are the loser", correct)
        break
