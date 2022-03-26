class Employee():
    def __init__(self, ID="", rate=0.0):
        self.__ID = ID
        self.__rate = rate
        self.__hours = 0

    # Returns a string representation of the Employee Object
    def __str__(self):
        mystr = f"Employee ID: {self.__ID}\n"
        mystr += f"Hourly Rate: {self.__rate}\n"
        mystr += f"Hours Worked: {self.__hours}\n"
        mystr += f"Gross Wages: {self.getWages()}\n"
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
