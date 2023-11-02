#!/usr/bin/python3 

import sys

def modulo_two(n):
	result = 1
	for k in range(n):
		result = result * 2 % 1000000
	return result

with open(sys.argv[1]) as input_:
	n = int(input_.readline().strip())
	print(modulo_two(n))

