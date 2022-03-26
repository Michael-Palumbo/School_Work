import datetime

class Receipt:

	def __init__(self, tax_rate):
		self.__tax_rate = tax_rate
		self.__purchases = []

	def __str__(self):
		total_cost = 0
		total_tax = 0
		out = '----- ' +'Receipt ' +str(datetime.datetime.now()) +' -----'
		for item in self.__purchases:
			out += '\n' +str(item)
			total_cost += item.getPrice()
			total_tax += item.getTax(self.__tax_rate)
		out += '\nSub Total___________________________' +"${:.2f}".format(total_cost)
		out += '\nTax_________________________________' +"${:.2f}".format(total_tax)
		out += '\nTotal_______________________________' +"${:.2f}".format(total_cost + total_tax)
		return out

	def addItem(self, item):
		self.__purchases.append(item)
