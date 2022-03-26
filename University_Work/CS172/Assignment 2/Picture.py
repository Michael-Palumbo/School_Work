from Media import *

class Picture(Media):

    def __init__(self, type, name, rating, Resolution):
        super().__init__(type, name, rating)
        self.__Resolution = Resolution

    def show(self):
        print("Showing \"" + super().getName() + "\"\n")

    # Calls the inherited string method and then attaches it's own attributes
    def __str__(self):
        s = super().__str__()
        s += "Resolution: \""+ str(self.__Resolution) + "\"\n"

    # Getter
    def getResolution(self):
        return self.__Resolution

    # Setter
    def setResolution(self, r):
        self.__Resolution = r
