#!/usr/bin/python3 

import sys

with open(sys.argv[1]) as input_:
	a, b, c, d, e, f = list(map(int, input_.readline().strip().split(" ")))
	S = a+b+c+d+e+f
	#print((2*(a**2 + b**2 + c**2) + 1.5*(d**2) + e**2))# / S)
	print(2*(a+b+c) + 1.5*d + e)
