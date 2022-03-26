class Employee():
    def __init__(self, ID="", rate=0.0):
        self.__hours = 0.0
        self.__ID = ID
        self.__rate = rate

    def __str__(self):
        mystr = ""
        mystr += f"Employee ID: {self.getID()}\n"
        mystr += f"Hourly Rate: {self.getRate()}\n"
        mystr += f"Hours Worked: {self.getHours()}\n"
        mystr += f"Gross Wages: {self.getWages()}\n"
        return mystr

    def getID(self):
        return self.__ID

    def setID(self, ID):
        self.__ID = ID

    def getRate(self):
        return self.__rate

    def setRate(self, rate):
        self.__rate = rate

    def getHours(self):
        return self.__hours

    def setHours(self, hours):
        self.__hours = hours

    def getWages(self):
        return self.__hours * self.__rate
