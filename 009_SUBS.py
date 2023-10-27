#!/usr/bin/python3 

import sys

with open(sys.argv[1]) as input_:
	positions = list()
	template = input_.readline().strip()
	motif = input_.readline().strip()
	for k in range(len(template) - len(motif)):
		if template[k:k + len(motif)] == motif:
			positions.append(k + 1)

print(*positions)
