# Doubly Linked Nodes
class Node():
    def __init__(self, value, next = None, prev = None):
        self.__value = value
        self.__next = next
        self.__prev = prev

    def __str__(self):
        return str(self.__value)

    # Refernce to Next Node
    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    # Reference to Prev Node
    def getPrev(self):
        return self.__prev

    def setPrev(self, prev):
        self.__prev = prev

    # Value of the Node (Contains an Employee)
    def getValue(self):
        return self.__value
