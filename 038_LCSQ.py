#!/usr/bin/python3 
# multiple sequence alignment

import sys
import numpy as np
np.set_printoptions(edgeitems=36, linewidth=10000)

def mat_min(arr):
	if arr.size == 0:
		return 0
	else:
		return arr.min()

def mat_max(arr):
	if arr.size == 0:
		return 0
	else:
		return arr.max()

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

seq_a, seq_b = sorted(sequences.values(), key=lambda x:len(x), reverse=True)
# seq_a: column, seq_b: row
path_mat = np.zeros((len(seq_b), len(seq_a)))
for j, nuc_b in enumerate(seq_b):
	for k, nuc_a in enumerate(seq_a):
		if nuc_a == nuc_b:
			path_mat[j, k] = mat_max(path_mat[:j, :k]) + 1

#print(path_mat)

length = 9999
coordinate = path_mat.shape
sequence = ""
while length > 1:
	x, y = coordinate
	coordinate = tuple([k[0] for k in np.where(path_mat[:x, :y] == mat_max(path_mat[:x, :y]))])
	length = path_mat[coordinate]
	#print(coordinate, length, seq_a[coordinate[0]])
	sequence += seq_b[coordinate[0]]

print(sequence[::-1])
