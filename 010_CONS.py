#!/usr/bin/python3 

import sys

sequences = dict()
with open(sys.argv[1]) as input_:
	seq_name = ""
	for line in input_:
		line = line.strip()
		if line.startswith(">"):
			seq_name = line[1:]
			sequences[seq_name] = ""
		else:
			sequences[seq_name] += line

base_order = ("A", "C", "G", "T")
profile_matrix = {k:list() for k in base_order}
consensus = ""
for bases in zip(*sequences.values()):
	base_counts = {k:0 for k in base_order}
	for base in bases:
		base_counts[base] += 1
	for base in base_order:
		profile_matrix[base].append(base_counts[base])
	consensus += max(base_counts, key=lambda x:base_counts[x])

print(consensus)
for base in base_order:
	print(f"{base}:", *profile_matrix[base])

