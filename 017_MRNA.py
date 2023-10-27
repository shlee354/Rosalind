#!/usr/bin/python3 

import sys

codon_xref = dict()
with open("codon_table") as codon_table:
	for line in codon_table:
		codon, aa = line.strip().split("\t")
		if aa not in codon_xref:
			codon_xref[aa] = 1
		else:
			codon_xref[aa] += 1

with open(sys.argv[1]) as input_:
	protein_string = input_.readline().strip()
	result = 1
	for aa in protein_string:
		result *= codon_xref[aa]
		if result >= 1000000:
			result = result % 1000000
	print((result * 3) % 1000000)
