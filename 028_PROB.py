#!/usr/bin/python3 

import sys
from functools import reduce  # Required in Python 3
import operator
from math import log

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

with open(sys.argv[1]) as input_:
	dna_string = input_.readline().strip()
	gc_contents = list(map(float, input_.readline().strip().split(" ")))
	results = [log(prod([gc_prob/2 if k in ("G","C") else (1-gc_prob)/2 for k in dna_string]), 10) for gc_prob in gc_contents]

print(*results)
