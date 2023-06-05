class Dog:
    def __init__(self, name="Barsik", height=20, weight=30, age=10, master="Maxim", address="Minsk"):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__address = address

    def jump(self):
        print("Jump!")

    def run(self):
        print("Run!")

    def bark(self):
        print("Bark!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
