#!/usr/bin/python3 

import sys
from itertools import product

with open(sys.argv[1]) as input_:
	symbols = input_.readline().strip().split(" ")
	n = int(input_.readline().strip())
	for substr in sorted(product(symbols, repeat=n)):
		print("".join(substr))
