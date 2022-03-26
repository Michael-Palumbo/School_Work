#!/bin/usr/env python3
#Michael Palumbo
#Demonstrating Concatinating by copying values
#Jan, 21, 2020

from cell import Cell
from cell import list2string
def concat_copy( list1, list2 ):
	temp = Cell( list1.data)
	tempRef = temp

	while list1.next != None:
		temp.next = Cell( list1.next.data )
		list1 = list1.next
		temp = temp.next

	temp.next = Cell( list2.data )
	temp = temp.next
	while list2.next != None:
		temp.next = Cell (list2.next.data)
		list2 = list2.next
		temp = temp.next

	return tempRef

if __name__ == "__main__":
	a = Cell( 13 )
	print( "c is holding: " + list2string( a ))
	b = Cell( 12, a )
	print(  "d is holding: " + list2string( b ))
	c = Cell( 1 )
	print( "c is holding: " + list2string( c ))
	d = Cell( 2, c )
	print(  "d is holding: " + list2string( d ))
	print( "concat is: " + list2string( concat_copy(b, d)))
