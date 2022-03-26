#lecture notes
class Node():
    def __init__(self, data, next = None, prev = None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def __str__(self):
        return str(self.__data)

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def getPrev(self):
        return self.__prev

    def setPrev(self, prev):
        self.__prev = prev

    def getData(self):
        return self.__data
