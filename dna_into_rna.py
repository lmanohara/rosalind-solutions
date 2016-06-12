"""
Transcribing DNA into RNA
"""
import fileinput

for dna in fileinput.input("rosalind_rna.txt"):
	rna = dna.replace("T", "U")
	print(rna)
