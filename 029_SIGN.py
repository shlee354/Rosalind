#!/usr/bin/python3 

import sys
from itertools import permutations, product
from operator import mul

result = list()
with open(sys.argv[1]) as input_:
	n = int(input_.readline().strip())
	sign_array = list(product((1,-1), repeat=n))
	for perm in permutations(range(1, n+1), n):
		for sign in sign_array:
			result.append(list(map(mul, perm, sign)))

print(len(result))
for k in result:
	print(*k)
