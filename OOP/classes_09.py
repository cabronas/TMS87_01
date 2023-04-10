class Dinosaur:
    def __init__(self, name="T-Rex", weight=200, subtype="Theropod"):
        self.name = name
        self.weight = weight
        self.subtype = subtype

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