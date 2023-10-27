#!/usr/bin/python3 

import sys
import re
import os
# without re: N{P}[ST]{P} -> find N -> next is not P -> next is S or T -> next is not P
# with re: N^P[ST]^P

protein_list = [(_.strip(), _.strip().split("_")[0]) for _ in open(sys.argv[1]) if _.strip()]
motif = re.compile("N[^P][ST][^P]")

if not os.path.isdir("uniprot"):
	os.mkdir("uniprot")

for protein, short in protein_list:
	if not os.path.isfile(f"uniprot/{short}.fasta"):
		os.system(f"wget -O uniprot/{short}.fasta http://www.uniprot.org/uniprot/{short}.fasta")

for protein, short in protein_list:
	sequence = ""
	with open(f"uniprot/{short}.fasta") as input_:
		for line in input_:
			if line.startswith(">"):
				pass
			else:
				sequence += line.strip()

	if motif.search(sequence):
		print(protein)
		print(*[k.start()+1 for k in re.finditer(r'(?=(N[^P][ST][^P]))', sequence)])
