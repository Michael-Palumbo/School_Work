#!/usr/bin/env python3

import sys, timeit
from prob1 import fib
from prob2 import fib2, reset_mem

def help_fib(i):
	fib(i)

def help_fib2(i):	
	fib2(i)

def write_to(filename, contents):
	f = open(filename, "w")
	for line in contents:
		f.write(line + "\n")
	f.close()

if __name__ == '__main__':
	fib1_contents = []
	fib2_contents = []
	for i in range(5,41,5):
		fib1_timer = timeit.Timer('help_fib(i)','from __main__ import help_fib, i')
		fib1_contents.append(str(i)+ " " + str(fib1_timer.timeit(1)))
	write_to("1.out",fib1_contents)
	for i in range(450, 951, 50):
		fib2_timer = timeit.Timer('help_fib2(i)','from __main__ import help_fib2, i')
		fib2_contents.append(str(i)+ " " + str(fib2_timer.timeit(1000)))
		reset_mem()
	write_to("2.out",fib2_contents)

