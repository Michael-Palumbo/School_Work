from receipt import *
from item import *
print("Welcome to Receipt Creator")

Receipt = receipt(.07)
while True:
    name = input("Enter Item Name: ")
    price = input("Enter Item Price: ")
    taxable = input("is the item taxable(yes/no): ").lower() == "yes"
    Receipt.addItem(item(name,price,taxable))
    if input("Add another item (yes/no): ") != "yes":
        break

print(Receipt)
