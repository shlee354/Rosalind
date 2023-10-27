#!/usr/bin/python3 

import sys

with open(sys.argv[1]) as input_:
	distance = 0
	dna_first = input_.readline().strip()
	dna_second = input_.readline().strip()
	for a,b in zip(dna_first, dna_second):
		if a != b:
			distance += 1

print(distance)
