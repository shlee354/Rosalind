#!/usr/bin/python3 

import sys

def fib(n, k):
	if n in (1,2):
		return 1
	else:
		return fib(n-1, k) + (k * fib(n-2, k))

with open(sys.argv[1]) as input_:
	n, k = list(map(int, input_.readline().strip().split(" ")))
	print(fib(n, k))
