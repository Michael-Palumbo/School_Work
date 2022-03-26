from Node import *
from LinkedList import *
from Employee import *

if __name__ == "__main__":

    Linked_List = LinkedList()

    # MAIN WHILE LOOP
    while True:
        print("*** CS 172 Payroll Simulator ***")
        print("a. Add New Employee")
        print("b. Enter Hours Worked")
        print("c. Display Payroll")
        print("d. Update Employee Hourly Rate")
        print("e. Remove Employee from Payroll")
        print("f. Exit the program")
        inp = input("Enter your choice: ")

        # MAKE A NEW EMPLOYEE
        if inp.lower() == "a":
            try:
                employee = Employee(input("Enter the new employee ID: "), float(input("Enter the hourly rate: ")))
                Linked_List.append(employee)
            except:
                print("Invalid: Plz Enter Valid Input")

        # CHANGE EMPLOYEES HOURS
        elif inp.lower() == "b":
            for employee in Linked_List:
                try:
                    employee.setHours(float(input(f"Enter hours worked for employee {employee.getID()}: ")))
                except:
                    print("Invalid: Not a number")

        # DISPLAY ALL PAYROLL
        elif inp.lower() == "c":
            print(Linked_List)

        # CHANGE RATES OF EMPLOYEES
        elif inp.lower() == "d":
            for employee in Linked_List:
                try:
                    employee.setRate( float(input(f"Enter new rate worked for employee {employee.getID()}: ")))
                except:
                    print("Invalid: Not a number")

        # REMOVE AN EMPLOYEE
        elif inp.lower() == "e":
            Linked_List.remove(input("Enter the ID of the employee to remove from payroll: "))
            print("Done.")

        # QUIT THE GAME
        elif inp.lower() == "f":
            print("Good-Bye!")
            break

        print()
