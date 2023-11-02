#!/usr/bin/python3 

import sys
from itertools import product

with open(sys.argv[1]) as input_:
	alphabets = input_.readline().strip().split(" ")
	n = int(input_.readline().strip())
	custom_order = dict(zip(alphabets, range(len(alphabets))))
	for seq in sorted([i for j in [list(product("".join(alphabets),repeat=k)) for k in range(1,n+1)] for i in j], key=lambda x:[custom_order[y] for y in x]):
		print("".join(seq))
