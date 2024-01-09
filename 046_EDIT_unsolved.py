#!/usr/bin/python3 

import sys

def edit_dist(a, b):


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

