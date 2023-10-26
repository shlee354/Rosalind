#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_:
	dna_string = input_.readline()
	base_counts = [dna_string.count(k) for k in ("A","C","G","T")]
	print(*base_counts)
