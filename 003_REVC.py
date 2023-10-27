#!/usr/bin/python3 

import sys

complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
with open(sys.argv[1]) as input_:
	print("".join(complement.get(k, "") for k in input_.readline()[::-1]))
