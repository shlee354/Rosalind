#!/usr/bin/python3 

import sys

with open(sys.argv[1]) as input_:
	k, m, n = list(map(int, input_.readline().strip().split(" ")))
	A = k+m+n
	print((k/A) + (m*(0.75*(m-1)) + m*k + n*k + m*n) / (A * (A-1)))
