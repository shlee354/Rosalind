#!/usr/bin/python3 

import sys

codon_table = {a:b for a,b in (line.strip().split("\t") for line in open("codon_table"))}

names = list()
sequences = dict()
with open(sys.argv[1]) as input_:
	seq_name = ""
	for line in input_:
		line = line.strip()
		if line.startswith(">"):
			seq_name = line[1:]
			names.append(seq_name)
			sequences[seq_name] = ""
		else:
			sequences[seq_name] += line

sequence = sequences.pop(names[0])
for intron in sequences.values():
	sequence = sequence.replace(intron, "|")

sequence = sequence.replace("|","").replace("T","U")

protein = ""
for k in range(0, len(sequence), 3):
	amino_acid = codon_table[sequence[k:k+3]]
	if amino_acid == "Stop":
		break
	protein += amino_acid

print(protein)
