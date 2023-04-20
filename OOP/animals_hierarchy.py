from abc import *


class Animal(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abstractmethod
    def action(self):
        raise NotImplementedError


class Feline(ABC):
    @abstractmethod
    def scratch(self):
        raise NotImplementedError


class Canine(ABC):
    @abstractmethod
    def howl(self):
        raise NotImplementedError


class Pet(Animal):

    def __init__(self, name, master):
        super().__init__(name)
        self.__master = master

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master


class Cat(Pet, Feline):
    def __init__(self, name, master, weight):
        super().__init__(name, master)

    def action(self):
        print("Meow")

    def scratch(self):
        print("Scratch")


class Dog(Pet, Canine):
    def __init__(self, name, master, weight):
        super().__init__(name, master)

    def action(self):
        print("Woof")

    def howl(self):
        print("Howl")


class WildAnimal(Animal):

    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


class Lion(WildAnimal, Feline):
    def __init__(self, name, height, weight):
        super().__init__(name, height)
        self.__weight = weight

    def action(self):
        print("Roar")

    def scratch(self):
        print("Scratch")


class Wolf(WildAnimal, Canine):
    def __init__(self, name, height, weight):
        super().__init__(name, height)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def action(self):
        print("Woof")

    def howl(self):
        print("Howl")
