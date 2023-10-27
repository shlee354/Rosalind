#!/usr/bin/python3 

import sys

mat_rab = {0:1, 1:0, 2:1} # too many recursive call; memoization was imperative
# n < m+1: rabbits won't die before this generation
# n = m+1: the first rabbit dies
def mature_rabbit(n):
	if n < 0:
		return 0
	if n not in mat_rab:
		mat_rab[n] = mature_rabbit(n-1) + mature_rabbit(n-2) - mature_rabbit(n-m-1)
	return mat_rab[n]

with open(sys.argv[1]) as input_:
	n, m = list(map(int, input_.readline().strip().split(" ")))
	print(mature_rabbit(n) + mature_rabbit(n-1))

