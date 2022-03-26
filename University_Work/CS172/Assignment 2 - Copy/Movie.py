from Media import *

class Movie(Media):

    def __init__(self, type, name, rating, dir, runningTime):
        super().__init__(type, name, rating)
        self.__Director = dir
        self.__RTime = runningTime

    # Calls the super string so we don't type the type, name
    def __str__(self):
        s = super().__str__()
        s +=  "Director: " + self.__Director
        s += "\nRunning Time: " + self.__RTime + "\n"
        return s

    def play(self):
        print(super().getName() + ", playing now\n")

    # Getters
    def getDirector(self):
        return self.__Director

    def getRunTime(self):
        return self.__RunTime

    # Setters
    def setDirector(self, d):
        self.__Director = d

    def setRunTime(self, rt):
        self.__RunTime = rt
