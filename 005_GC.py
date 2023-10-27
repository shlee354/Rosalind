#!/usr/bin/python3 

import sys

def gc_content(dna):
	
	return (dna.count("G") + dna.count("C")) / len(dna) * 100

sequences = dict()
with open(sys.argv[1]) as input_:
	seq_name = ""
	for line in input_:
		line = line.strip()
		if line.startswith(">"):
			seq_name = line[1:]
			sequences[seq_name] = ""
		else:
			sequences[seq_name] += line

gc_contents = sorted([(k, gc_content(v)) for k,v in sequences.items()], key=lambda x:x[1], reverse=True)
print(*gc_contents[0], sep="\n")
