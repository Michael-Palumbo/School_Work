
class Media():

    def __init__(self, type, name, rating):
        self.__Type = type
        self.__Name = name
        self.__Rating = rating

    # Return String representation
    def __str__(self):
        s = "Type: "+ self.__Type +"\n"
        s += "Name: " + self.__Name + "\n"
        s += "Rating: " + self.__Rating + " out of 5 Stars\n"
        return s

    def __repr__(self):
        return str(self)

    # Getters
    def getType(self):
        return self.__Type

    def getName(self):
        return self.__Name

    def getRating(self):
        return self.__Rating

    # Setters
    def setType(self, t):
        self.__Type = t

    def setName(self, n):
        self.__Name = n

    def setRating(self, r):
        self.__Rating = r
