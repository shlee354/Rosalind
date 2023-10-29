#!/usr/bin/python3 

import sys

def transited(a, b):
	if (a, b) in (("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")):
		return True
	else:
		return False

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

first = sequences[sequence_name[0]]
second = sequences[sequence_name[1]]

transition = 0
transversion = 0
for a, b in zip(first, second):
	if a == b:
		pass
	elif transited(a, b):
		transition += 1
	else:
		transversion += 1

print(transition/transversion)
