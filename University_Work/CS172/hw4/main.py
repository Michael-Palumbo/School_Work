from Node import *
from LinkedList import *
from Employee import *
if __name__ == "__main__":

    Linked_list = LinkedList()

    while True:
        print("*** CS 172 Payroll Simulator ***")
        print("a. Add New Employee")
        print("b. Enter Hours Worked")
        print("c. Display Payroll")
        print("d. Update Employee Hourly Rate")
        print("e. Remove Employee from Payroll")
        print("f. Exit the program")
        inp = input("Enter your choice: ")

        #<== Add a new Employee ==>
        if inp == "a":
            try:
                enterID = input("Enter the new employee ID: ")

                # Rate needs to be a float, so we put it in a try except
                enterRate = float(input("Enter the hourly rate: "))
                employee = Employee(enterID, enterRate)
                Linked_list.append(employee)
            except:
                print("Rate must be a float or string")

        #<== Give an Employee Hours ==>
        elif inp == "b":
            for i in Linked_list:
                eID = i.getID()
                try:
                    i.setHours( int(input("Enter hours worked for employee " + str(eID) + " : ")))
                except:
                    print("Plz enter hours as a number")

        #<== Print out payroll of All Employees ==>
        elif inp == "c":
            print(Linked_list, end="")

        #<== Remove an Employee ==>
        elif inp == "e":
            remove_ID = input("Enter the ID of the employee to remove from payroll: ")
            Linked_list.remove(remove_ID)

        #<== Quit ==>
        elif inp == "f":
            break
