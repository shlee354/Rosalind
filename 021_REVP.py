#!/usr/bin/python3 

import sys
import re

def reverse_complement(s):
	complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
	return "".join([complement[k] for k in s])[::-1]

sequence = ""
with open(sys.argv[1]) as input_:
	for line in input_:
		if line.startswith(">"):
			pass
		else:
			sequence += line.strip()

for k in range(4, 13, 2):
	for j in range(len(sequence)-k+1):
		substr = sequence[j:j+k]
		if len(substr) == k and (substr[:k//2] == reverse_complement(substr[k//2:])):
			print(j+1, k)
