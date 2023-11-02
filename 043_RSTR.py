#!/usr/bin/python3 

import sys
from functools import reduce  # Required in Python 3
import operator
from math import log

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

with open(sys.argv[1]) as input_:
	elements = input_.readline().strip().split(" ")
	n = int(elements[0])
	gc_prob = float(elements[1])
	dna_string = input_.readline().strip()
	dna_prob = prod([gc_prob/2 if k in ("G","C") else (1-gc_prob)/2 for k in dna_string])

	print(1 - (1 - dna_prob) ** n)
