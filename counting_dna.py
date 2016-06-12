"""
Counting DNA Nucleotides
"""
import fileinput

for dna in fileinput.input("counting_point_mutations.txt"):
	for i in 'ACGT':
		print dna.count(i),

