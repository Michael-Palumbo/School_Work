from Receipt import Receipt
from Item import Item

print('Welcome to Receipt Creator')
more = True

r = Receipt(0.06)

while more:
	name = input('Enter Item Name: ')
	price = float(input('Enter Item Price: '))
	taxable = True if input('Is the item taxable (yes/no): ') == 'yes' else False
	more =  True if input('Add another item (yes/no): ') == 'yes' else False
	r.addItem(Item(name, price, taxable))
	
print(str(r))
