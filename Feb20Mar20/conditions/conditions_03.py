"""
Запросить у пользователя возраст. Если возраст меньше 0 - вывести Wrong input,
если меньше 18 - вывести Cola, иначе - вывести Beer
"""
s = input("Enter your age: ")
age = int(s)
if age < 0:
    print("Wrong input")
elif age < 18:
    print("Cola")
else:
    print("Beer")
