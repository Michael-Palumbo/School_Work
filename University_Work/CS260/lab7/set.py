#!/usr/bin/env python3

"""
Michael Palumbo
2/24/20
CS260
HW7
"""
class DSS:
	def __init__(self, value):
		self.value = value
		self.parent = self #links back to itself
		self.height = 0

def Initialize(array):
	temp = []
	for a in array:
		temp.append( DSS(a) )
	return temp

def Find(array, value):
	#node = array[node]
	node = None

	for n in array:
		if n.value == value:
			node = n
			break

	if node == None: #element isn't even in set
		return None

	if node.parent != node:
		node.parent = Find(array, node.parent.value)
	return node.parent

def Merge(array, x, y): #the array is uneeded since nodes can give context
	xRoot = Find(array, x)
	yRoot = Find(array, y)

	if xRoot == yRoot:
		return #they are already in the same set

	if xRoot.height < yRoot.height:
		xRoot, yRoot = yRoot, xRoot #swap roots, to make it simpler we can just act on one root

	yRoot.parent = xRoot
	if xRoot.height == yRoot.height:
		xRoot.height += 1

