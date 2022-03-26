class Item:

	def __init__(self, name, price, taxable):
		self.__name = name
		self.__price = price
		self.__taxable = taxable
		
	def __str__(self):
		return self.__name +'_____________________________' +"${:.2f}".format(self.__price)

	def getPrice(self):
		return self.__price

	def getTax(self, tax_rate):
		return self.__price * tax_rate if self.__taxable else 0