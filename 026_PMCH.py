#!/usr/bin/python3 

import sys
from math import factorial as f

sequence = ""
with open(sys.argv[1]) as input_:
	for line in input_:
		if line.startswith(">"):
			pass
		else:
			sequence += line.strip()

n_a = sequence.count("A")
n_c = sequence.count("C")

print(f(n_a) * f(n_c))
