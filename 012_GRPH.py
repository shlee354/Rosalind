#!/usr/bin/python3 

import sys
from itertools import permutations

n = 3
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

edges = list()
for a, b in permutations(sequences, 2):
	seq_a = sequences[a]
	seq_b = sequences[b]
	if seq_a[len(seq_a)-n:] == seq_b[:n]:
		edges.append((a, b))

for edge in edges:
	print(*edge)
