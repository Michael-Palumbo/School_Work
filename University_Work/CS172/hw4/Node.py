
class Node():
    def __init__(self, value, next = None):
        self.__value = value
        self.__next = next

    def __str__(self):
        return str(self.__value)

    # Reference to It's Next Node
    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def getValue(self):
        return self.__value

    def setValue(self):
        return self.__value
