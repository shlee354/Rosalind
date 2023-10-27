#!/usr/bin/python3 

import sys

with open(sys.argv[1]) as input_:
	print(input_.readline().replace("T","U"))
