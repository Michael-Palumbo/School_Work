from Node import Node

class LinkedList():
    def __init__(self):
        self.__head = None

    # Add a new Employee at the end of the linked list
    def append(self, data):
        newNode = Node(data)
        if self.__head == None:
            self.__head = newNode
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            # Exchange References
            current.setNext(newNode)
            newNode.setPrev(current)

    # Removes a specified id from the linked list
    def remove(self, data):
        current = self.__head
        while current != None:
            if current.getValue().getID() == data:
                if current.getPrev() != None:
                    current.getPrev().setNext(current.getNext())
                if current.getNext() != None:
                    current.getNext().setPrev(current.getPrev())
                if current == self.__head:
                    self.__head = self.__head.getNext()
                break
            else:
                #print(current.getValue().getID())
                current = current.getNext()

    # Prints the string representation of the linked list, which in this case is the payroll
    def __str__(self):
        temp = self.__head
        mystr = "\n*** Payroll ***\n"
        while temp != None:
            mystr += f"{temp}\n"
            temp = temp.getNext()
        return mystr

    # Overloaded length operator, just prints out length of the linked list
    def __len__(self):
        temp = self.__head

        if self.__head == None:
            return 0
        count = 1
        while temp.getNext() != None:
            temp = temp.getNext()
            count += 1
        return count

    # Overload the square bracket operator
    def __getitem__(self, index):
        if index >= len(self):
            print("Index out of bounds")
            return None
        current = self.__head
        for i in range(index):
            current= current.getNext()

        return current.getValue()
