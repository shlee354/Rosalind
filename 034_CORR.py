#!/usr/bin/python3 

import sys

def hamming_dist(a, b):
	return sum([x != y for x, y in zip(a, b)])

def complement(x):
	if x == "A":
		return "T"
	elif x == "T":
		return "A"
	elif x == "G":
		return "C"
	elif x == "C":
		return "G"

def reverse_complement(a):
	return "".join([complement(k) for k in a][::-1])

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

original_seq = dict()
for sequence in sequences.values():
	original_seq[sequence] = original_seq.get(sequence, 0) + 1

correct_reads = set() # critical
for sequence in sequences.values():
	count = original_seq[sequence] + original_seq.get(reverse_complement(sequence), 0)
	if count > 1:
		correct_reads.add(sequence)

for sequence in sequences.values():
	count = original_seq[sequence] + original_seq.get(reverse_complement(sequence), 0)
	if count == 1:
		for template in correct_reads:
			if hamming_dist(template, sequence) == 1:
				print(f"{sequence}->{template}")
				break
			rc_template = reverse_complement(template)
			if hamming_dist(rc_template, sequence) == 1:
				print(f"{sequence}->{rc_template}")
				break
