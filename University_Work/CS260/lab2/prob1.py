#!/bin/usr/env python3
#Michael Palumbo
#Demonstrating Concat
#Jan, 21, 2020

from cell import Cell
from cell import list2string
def concat( list1, list2 ):
	list1Ref = list1

	while list1.next != None:
		list1 = list1.next

	list1.next = list2

	return list1Ref

if __name__ == "__main__":
	a = Cell( 13 ) 
	print( "c is holding: " + list2string( a )) 
	b = Cell( 12, a )
	print(  "d is holding: " + list2string( b ))
	c = Cell( 1 )
	print( "c is holding: " + list2string( c ))
	d = Cell( 2, c )
	print(  "d is holding: " + list2string( d ))
	print( "concat is: " + list2string(concat(b, d)))
