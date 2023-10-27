#!/usr/bin/python3 

import sys
#from math import comb # above 3.8
from math import factorial as f

def comb(n, r):
	return f(n) // f(r) // f(n-r)

with open(sys.argv[1]) as input_:
	k, N = list(map(int, input_.readline().strip().split(" ")))
	K = 2 ** k
	print(sum([comb(K, n) * (0.25**n) * (0.75**(K-n)) for n in range(K, N-1, -1)]))
