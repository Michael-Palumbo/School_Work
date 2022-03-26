class receipt:
    def __init__(self, tax):
        self.__purchases = []
        self.__tax = tax
        #print("{:_<25} Made Reciept".format("L"))
    def __str__(self):
        import datetime
        s = "----Receipt %s ----\n"%(datetime.datetime.now())
        total_cost, total_tax = 0, 0
        for i in self.__purchases:
            s += str(i)
            total_cost += i.getPrice()
            total_tax += i.getTax(self.__tax)

        s += '\n'

        s += "{:_<33}{:.2f}\n".format("Sub Total",total_cost)
        s += "{:_<33}{:.2f}\n".format("Tax",total_tax)
        s += "{:_<33}{:.2f}\n".format("Total",total_cost + total_tax)
        #s += "Sub Total" + "_"*29 + "%.2f"%self.getTotal()
        #s += "Tax" + "_"*33 + "%.2f"%self.getTotal()
        #s += "Total" + "_"*32 + "%.2f"%(self.getTotal()+self.getTaxTotal())

        return s


    def addItem(self,item):
        self.__purchases.append(item)
