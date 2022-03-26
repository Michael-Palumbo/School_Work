from Media import *

class Picture(Media):

    def __init__(self, type, name, rating, Resolution):
        super().__init__(type, name, rating)
        self.__Resolution = Resolution

    def show(self):
        print("Showing " + super().getName() + "\n")

    # Calls the super string so we don't type the type, name
    def __str__(self):
        s = super().__str__()
        s += "Resolution:" +str(self.__Resolution) + "\n"
        return s

    # Getter
    def getResolution(self):
        return self.__Resolution

    # Setter
    def setResolution(self, r):
        self.__Resolution = r
