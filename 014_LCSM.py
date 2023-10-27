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

shortest = sequences.pop(sorted(sequences, key=lambda x:len(sequences[x]))[0])
for k in range(len(shortest), 1, -1):
	for j in range(len(shortest)-k+1):
		substr = shortest[j:j+k]
		#if all([substr in seq for seq in sequences.values()]):
		if all([seq.find(substr) != -1 for seq in sequences.values()]):
			print(substr)
			exit()
