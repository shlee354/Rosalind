#!/usr/bin/python3 

import sys
#from math import comb # above 3.8
from math import factorial as f

f_values = {0:1}
def f_mod(n):
	if n == 0:
		return 1
	if n not in f_values:
		f_values[n] = (n * f_mod(n-1))# % 1000000
	return f_values[n]

def modulo_two(n):
	result = 1
	for k in range(n):
		result = result * 2 % 1000000
	return result

with open(sys.argv[1]) as input_:
	n, m = list(map(int, input_.readline().strip().split(" ")))
	for k in range(0, n, n//20):
		f_mod(k)
	print(sum([(f_mod(n) // f_mod(k) // f_mod(n-k)) % 1000000 for k in range(m, n+1)]) % 1000000)
