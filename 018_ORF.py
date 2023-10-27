#!/usr/bin/python3 

import sys
import re

codon_table = {a:b for a,b in (line.strip().split("\t") for line in open("codon_table"))}
complement = {"A":"U", "U":"A", "C":"G", "G":"C"}

sequence = ""
with open(sys.argv[1]) as input_:
	for line in input_:
		if line.startswith(">"):
			pass
		else:
			sequence += line.strip()
sequence = sequence.replace("T","U")
sequence_rev = "".join([complement[k] for k in sequence])[::-1]

proteins = set()
for match in re.finditer(r'AUG', sequence_rev):
	start_pos = match.start()
	protein = ""
	for k in range(start_pos, len(sequence_rev), 3):
		aa = codon_table.get(sequence_rev[k:k+3])
		if not aa:
			break
		if aa == "Stop":
			proteins.add(protein)
			break
		protein += aa

for match in re.finditer(r'AUG', sequence):
	start_pos = match.start()
	protein = ""
	for k in range(start_pos, len(sequence), 3):
		aa = codon_table.get(sequence[k:k+3])
		if not aa:
			break
		if aa == "Stop":
			proteins.add(protein)
			break
		protein += aa

for protein in proteins:
	print(protein)
