#!/usr/bin/env python3

import sys

def fib(n):
	if n <= 1:
		return 1
	return fib(n-2) + fib(n-1)

if __name__ == "__main__":
	print(fib(int(sys.argv[1])))

