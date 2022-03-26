#!/bin/usr/env python3 

from cell import Cell
from prob1 import *
from prob2 import *

import random
import time

def makeChart():
	w = open("data.out", "w")
	for i in range(1000, 15000,1000):
		list1 = makeCells(i)
		list2 = makeCells(i)
		start = time.time()
		concat(list1, list2)
		end = time.time()
		
		start1 = time.time()
		concat_copy(list1, list2)
		end1 = time.time()
		
		w.write("%d %.5f %.5f \n"%(i,end-start,end1-start1))
	w.close()

def makeCells( amount ):
	
	temp = Cell( random.randint(0,10000) )
	tempRef = temp
	for i in range(amount - 1):
		temp.next = Cell( random.randint(0, 10000))
		temp = temp.next

	return tempRef

if __name__ == "__main__":
	makeChart()
