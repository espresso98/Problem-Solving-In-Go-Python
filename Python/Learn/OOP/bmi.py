class BMI:
    __pHeight = 0
    __pWeight = 0

    def __getHeight(self):
        return self.__pHeight
    def __setHeight(self, inValue):
        self.__pHeight = inValue
    height = property(__getHeight,__setHeight)

    def __getWeight(self):
        return self.__pWeight
    def __setWeight(self, inValue):
        self.__pWeight = inValue
    weight = property(__getWeight,__setWeight)

    def BMI_value(self):
        return self.__pWeight / (self.__pHeight ** 2)

    def __eq__(self, other):
        return self.height == other.height and self.weight == other.weight