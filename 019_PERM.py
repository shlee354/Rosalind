#!/usr/bin/python3 

import sys
from itertools import permutations

with open(sys.argv[1]) as input_:
	n = int(input_.readline().strip())
	perms = list(permutations(range(1, n+1), n))
	print(len(perms))
	for k in perms:
		print(*k)
