#!/usr/bin/python3 

import sys

with open(sys.argv[1]) as input_:
	n, k = list(map(int, input_.readline().strip().split(" ")))
	result = 1
	for i in range(k):
		result = result * (n - i) % 1000000

print(result % 1000000)
