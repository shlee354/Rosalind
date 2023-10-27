#!/usr/bin/python3 

import sys

codon_table = {a:b for a,b in (line.strip().split("\t") for line in open("codon_table"))}

with open(sys.argv[1]) as input_:
	rna_string = input_.readline().strip()
	protein = ""
	for k in range(0, len(rna_string), 3):
		amino_acid = codon_table[rna_string[k:k+3]]
		if amino_acid == "Stop":
			break
		protein += amino_acid

print(protein)
