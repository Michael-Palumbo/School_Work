from Node import Node

class LinkedList():

    def __init__(self):
        # The Starting Node, Everything is based off this
        self.__head = None

    # Append An Element to the End of the Linked List
    def append(self, data):
        newNode = Node(data)
        # If head was never refereced
        if self.__head == None:
            self.__head = newNode

        else:
            current = self.__head
            # Get to last element in linked list
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)

    # Removes a node
    def remove(self,value):
        prev = None
        curr = self.__head
        while curr:
            if curr.getValue().getID() == value:
                if prev != None:
                    # Deference the previouse node of current, to the next node of current
                    prev.setNext(curr.getNext())
                else:
                    self.__head = curr.getNext()

            # Move onto the Node
            prev = curr
            curr = curr.getNext()

    # Return a string representation of the object
    def __str__(self):
        current = self.__head
        mystr = "*** Payroll ***" + "\n"
        while current != None:
            mystr += f"{current}\n"
            current = current.getNext()
        return mystr

    # Overload function, returns the length of the list
    def __len__(self):
        current = self.__head

        if self.__head == None:
            return 0

        count = 0
        # Loop to the end of list, the end will have a null value
        while current.getNext() != None:
            current = current.getNext()
            count += 1
        return count

    # Overloads the bracket operator e.i. [n]
    def __getitem__(self, index):
        if index >= len(self):
            print("Index out of bounds")
            return None
        current = self.__head
        for i in range(index):
            current= current.getNext()

        return current.getValue()
