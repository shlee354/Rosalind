#!/usr/bin/python3 

import sys

mass_table = {a:float(b) for a,b in (line.strip().split("\t") for line in open("mass_table"))}

with open(sys.argv[1]) as input_:
	protein_string = input_.readline().strip()
	print(sum([mass_table[k] for k in protein_string]))
