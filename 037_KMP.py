#!/usr/bin/python3 

import sys
from itertools import product

sequence = ""
with open(sys.argv[1]) as input_:
	next(input_)
	for line in input_:
		sequence += line.strip()

failure_array = [0] * len(sequence)
k = 1
current = ""
length_to_match = 1
while k < len(sequence):
	prefix = sequence[:k]
	substr = sequence[1:k+1]
	if prefix[:length_to_match] != substr[-length_to_match:]: # elongation failed
		for i in range(length_to_match-1, 0, -1):
			if current[:i] == substr[-i:]: # rematched
				current = substr[-i:]
				length_to_match = len(current) + 1 # elongate from here
				break
		else:
			current = "" # failed to rematch
			length_to_match = max(1, len(current))
		failure_array[k] = len(current)
	else: # try to elongate
		current += substr[-1]
		failure_array[k] = len(current)
		length_to_match += 1
	k += 1 

print(*failure_array)
