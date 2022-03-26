#!/usr/bin/env python3

import sys
import timeit

mem = [0]*1000

def reset_mem():
	mem = []

def fib2(n):
	if n <= 1:
		return 1

	if mem[n]:
		return mem[n] #value already saved, so return it

	mem[n] = fib2(n-2) + fib2(n-1)

	return mem[n]

if __name__ == "__main__":
	print(fib2(str(sys.argv[1])))
