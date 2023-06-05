"""
Переопределить методы change_weight, change_height в классе Parrot.
В случае непередачи параметра - вес изменяется на 0.05
"""
from animals import *
def main():
    parrot = Parrot("Pat", 2, "Maxim", 3, 3)
    print(parrot.name, parrot.age, parrot.master, parrot.weight, parrot.height)
    parrot.change_height()
    parrot.change_weight()
    print(parrot.name, parrot.age, parrot.master, parrot.weight, parrot.height)


if __name__ == "__main__":
    main()
