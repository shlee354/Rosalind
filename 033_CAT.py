#!/usr/bin/python3 

import sys
import re

complement = {"A":"U", "U":"A", "G":"C", "C":"G"}

catalan_number = {"":1, "AU":1, "UA":1, "GC":1, "CG":1} # memoization technique
def catalan_numbers(seq):

	if len(seq) <= 1:
		return 1
	else:
		if seq not in catalan_number:
			result = 0
			for k in [m.start() for m in re.finditer(complement[seq[0]], seq) if m.start() % 2 == 1]:
				result += (catalan_numbers(seq[1:k]) % 1000000) * (catalan_numbers(seq[k+1:]) % 1000000)
			catalan_number[seq] = result % 1000000
		return catalan_number[seq]

sequence = ""
with open(sys.argv[1]) as input_:
	next(input_)
	for line in input_:
		sequence += line.strip()

print(catalan_numbers(sequence) % 1000000)
