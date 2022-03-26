class item:
    def __init__(self, name, price, taxable):
        self.__name = name
        self.__price = float(price)
        self.__taxable = taxable

    def __str__(self):
         return "{:_<34}{:.2f}\n".format(self.__name,self.__price) 

    def getPrice(self):
        return self.__price

    def getTax(self, tax):
        return self.__price * tax if self.__taxable else 0
