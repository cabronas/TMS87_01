class Dinosaur:
    def __init__(self, name="T-Rex", height=200, subtype="Theropod"):
        self.__name = name
        self.__height = height
        self.__subtype = subtype

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
    def height(self, weight):
        self.__height = weight

    @property
    def subtype(self):
        return self.__subtype

    @subtype.setter
    def subtype(self, subtype):
        self.__subtype = subtype

    def jump(self, distance):
        print(f"Jumped {distance} meters")

    def grow(self, size):
        self.height += size
        print(f"Grew by {size} meters")
        print(f"Current height {self.height} meters")


class Bird:
    def __init__(self, name="Crow", weight=200, subtype="Common"):
        self.__name = name
        self.__weight = weight
        self.__subtype = subtype

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def subtype(self):
        return self.__subtype

    @subtype.setter
    def subtype(self, subtype):
        self.__subtype = subtype

    def fly(self, distance):
        print(f"Flew {distance} meters")

    def grow(self, weight):
        self.weight += weight
        print(f"Grew by {weight} kilograms")
        print(f"Current weight {self.weight} kilograms")


class Car:
    def __init__(self, name="Focus", max_speed=200, manufacturer="Ford"):
        self.__name = name
        self.__max_speed = max_speed
        self.__manufacturer = manufacturer

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def drive(self, hours):
        print(f"Drove {self.max_speed * hours} kilometers")

    def change_name(self, name):
        self.name = name
        print(f"Changed name to {name}")


class Student:
    def __init__(self, name="Maxim", clas=7, average_grade=8.1):
        self.__name = name
        self.__clas = clas
        self.__average_grade = average_grade

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def clas(self):
        return self.__clas

    @clas.setter
    def clas(self, clas):
        self.__clas = clas

    @property
    def average_grade(self):
        return self.__average_grade

    @average_grade.setter
    def average_grade(self, average_grade):
        self.__average_grade = average_grade

    def increase_grade(self):
        self.average_grade += 1
        print(f"Increased grade by one. Current grade: {self.average_grade}")

    def change_clas(self, clas):
        self.clas = clas
        print(f"Changed clas to {clas}")


class Laptop:
    def __init__(self, name="15HC6", processor="8750h", manufacturer="Lenovo"):
        self.__name = name
        self.__processor = processor
        self.__manufacturer = manufacturer

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, processor):
        self.__processor = processor

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def change_manufacturer(self,manufacturer):
        self.manufacturer = manufacturer
        print(f"Changed manufacturer to {manufacturer}")

    def change_processor(self, processor):
        self.processor = processor
        print(f"Changed processor to {processor}")
