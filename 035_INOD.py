#!/usr/bin/python3 

import sys

def num_internal_node(n):
	if n <= 2:
		return 0
	if n == 3:
		return 1
	else:
		return (n//2 + n%2) + num_internal_node(n//2)

with open(sys.argv[1]) as input_:
	n = int(input_.readline().strip())
	print(num_internal_node(n))
