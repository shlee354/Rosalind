#!/usr/bin/python3 

import sys
from itertools import product

sequence = ""
with open(sys.argv[1]) as input_:
	next(input_)
	for line in input_:
		sequence += line.strip()

kmers = dict()
for k in range(len(sequence)+1-4):
	kmer = sequence[k:k+4]
	kmers[kmer] = kmers.get(kmer, 0) + 1

print(*[kmers.get("".join(k), 0) for k in sorted(product("ATGC", repeat=4))])
