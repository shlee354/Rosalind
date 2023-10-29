#!/usr/bin/python3 

import sys
import re
from itertools import combinations

def superstring(a, b, n):

	a, b = sorted([a, b], key=lambda x:len(x), reverse=True)
	for first, second in ((a, b), (b, a)):
		substr = second[:n]
		for m in re.finditer(f"(?=({substr}))", first):
			suffix = first[m.start():]
			match_string = second[:len(suffix)]
			if suffix == match_string:
				return first[:m.start()] + second

	return None

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

overlap_length = sorted([len(k) for k in sequences.values()])[0] // 2

while len(sequences) > 1:
	for seq_a, seq_b in combinations(sequences.items(), 2):
		name_a, a = seq_a
		name_b, b = seq_b
		merged_seq = superstring(a, b, overlap_length)
		if merged_seq:
			sequences[name_a] = merged_seq
			sequences.pop(name_b)
			break

print(list(sequences.values())[0])
