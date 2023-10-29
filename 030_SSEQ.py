#!/usr/bin/python3 

import sys

sequences = dict()
sequence_name = list()
with open(sys.argv[1]) as input_:
	seq_name = ""
	for line in input_:
		line = line.strip()
		if line.startswith(">"):
			seq_name = line[1:]
			sequence_name.append(seq_name)
			sequences[seq_name] = ""
		else:
			sequences[seq_name] += line

dna_string = sequences[sequence_name[0]]
motif = sequences[sequence_name[1]]

pos_motif = 0
positions = list()
for k in range(len(dna_string)):
	if dna_string[k] == motif[pos_motif]:
		positions.append(k+1)
		pos_motif += 1
		if pos_motif == len(motif):
			break

print(*positions)
