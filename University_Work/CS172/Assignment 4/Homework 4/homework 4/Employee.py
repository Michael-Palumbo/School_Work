class Employee():
    def __init__(self, ID="", rate=0.0):
        self.__ID = ID
        self.__hours = 0
        self.__rate = rate

    def __str__(self):
        mystr = ""
        mystr += "Employee ID: " + str(self.__ID) + "\n"
        mystr += "Hourly Rate: " + str(self.__rate) + "\n"
        mystr += "Hours Worked: " + str(self.__hours) + "\n"
        mystr += "Gross Wages: " + str(self.getWages()) + "\n"
        return mystr

    def getID(self):
        return self.__ID

    def setID(self, ID):
        self.__ID = ID

    def getHours(self):
        return self.__hours

    def setHours(self, hours):
        self.__hours = hours

    def getRate(self):
        return self.__rate

    def setRate(self, rate):
        self.__rate = rate

    def getWages(self):
        return self.__hours * self.__rate

#a = Employee(12312, 3.0, 9.5)
#print(a)
