#!/usr/bin/python3 

import sys

def p_dist(a, b):
	return sum([x != y for x, y in zip(a, b)]) / len(a)

sequences = dict()
names = list()
with open(sys.argv[1]) as input_:
	seq_name = ""
	for line in input_:
		line = line.strip()
		if line.startswith(">"):
			seq_name = line[1:]
			sequences[seq_name] = ""
			names.append(seq_name)
		else:
			sequences[seq_name] += line

matrix = [[0 for i in range(len(names))] for j in range(len(names))]
# matrix =  [[0] * len(names)] * len(names) -> generate internally same list
values = dict()
for idx_a, name_a in enumerate(names):
	for idx_b, name_b in enumerate(names):
		#print(idx_a, name_a, idx_b, name_b)
		pair = tuple(sorted([name_a, name_b]))
		if idx_a == idx_b:
			pass
		else:
			matrix[idx_a][idx_b] = values.setdefault(pair, p_dist(sequences[name_a], sequences[name_b]))

for row in matrix:
	print(*row)
