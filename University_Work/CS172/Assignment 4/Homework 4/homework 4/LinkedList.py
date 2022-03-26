from Node import Node
#lecture notes
class LinkedList():
    def __init__(self):
        self.__head = None

    def append(self, data):
        temp1 = Node(data)
        if self.__head == None:
            self.__head = temp1
        else:
            temp = self.__head
            while temp.getNext() != None:
                temp = temp.getNext()
            temp.setNext(temp1)
            temp1.setPrev(temp)

    def remove(self, data):
        current = self.__head
        while current != None:
            if current.getData().getID() == data:
                if current.getNext() != None:
                    current.getNext().setPrev(current.getPrev())
                if current.getPrev() != None:
                    current.getPrev().setNext(current.getNext())
                current = None
                break
            else:
                print(current.getData().getID())
                current = current.getNext()

    def __str__(self):
        temp = self.__head
        mystr = "*** Payroll ***" + "\n"
        while temp != None:
            mystr += str(temp) + "\n"
            temp = temp.getNext()
        #mystr += "\n"
        return mystr


    def __len__(self):
        temp = self.__head

        if self.__head == None:
            return 0
        count = 1
        while temp.getNext() != None:
            temp = temp.getNext()
            count += 1
        return count


    def __getitem__(self, index):
        if index >= len(self):
            print("Index out of bounds")
            return None
        temp = self.__head
        for i in range(index):
            temp= temp.getNext()

        return temp.getData()
