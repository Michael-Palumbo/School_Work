#Q usr/bin/env Python3

#Michael Palumbo

import sys

inf = sys.maxsize

def getInput():
	inp = []
	for line in sys.stdin:
		inp.append(line)
	return inp

def buildGraph(data):
	n = len(data)	

	Graph = [[maxsize for i in range(n)] for i in range(5)]

	for line in data:
		
