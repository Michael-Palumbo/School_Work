from Node import *
from LinkedList import *
from Employee import *
if __name__ == "__main__":


    eList = LinkedList()
    #a = Employee(12312, 3.0, 9.5)
    ID = ""
    while True:
        print("*** CS 172 Payroll Simulator ***")
        print("a. Add New Employee")
        print("b. Enter Hours Worked")
        print("c. Display Payroll")
        print("d. Update Employee Hourly Rate")
        print("e. Remove Employee from Payroll")
        print("f. Exit the program")
        inp = input("Enter your choice: ")

        if inp.lower() == "a":
            try:
                enterID = input("Enter the new employee ID: ")

                enterRate = float(input("Enter the hourly rate: "))
                employee = Employee(enterID, enterRate)
                eList.append(employee)
            except:
                print("NO!")

        elif inp.lower() == "b":
            for i in range(len(eList)):
                eID = eList[i].getID()
                enterHours = int(input("Enter hours worked for employee " + str(eID) + " : "))
                eList[i].setHours(enterHours)
            #enterHours = input("Enter hours worked for employee %s")

        elif inp.lower() == "c":
            print(eList)

        elif inp.lower() == "e":
            removeID = input("Enter the ID of the employee to remove from payroll: ")
            eList.remove(removeID)
            print("Done.")

        print()
        #print(a.getHours())
