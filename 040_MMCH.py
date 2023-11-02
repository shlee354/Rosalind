#!/usr/bin/python3 

import sys
from math import factorial as f

def comb(n, r):
	return f(n) // f(r) // f(n-r)

sequence = ""
with open(sys.argv[1]) as input_:
	for line in input_:
		if line.startswith(">"):
			pass
		else:
			sequence += line.strip()

num_bases = {k:sequence.count(k) for k in "AUGC"}

s, l = sorted([num_bases["A"], num_bases["U"]])
au_pair = comb(l, s) * f(s)

s, l = sorted([num_bases["G"], num_bases["C"]])
gc_pair = comb(l, s) * f(s)

print(au_pair * gc_pair)
