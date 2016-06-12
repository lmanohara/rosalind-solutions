"""
Overlap Graphs
"""
import fileinput
from Bio import SeqIO

sequence_dictonary = []
file = open("rosalind_grph.fasta")
fasta_sequences = SeqIO.parse(file,'fasta')
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)
    sequence_dictonary.append((name, sequence))


for name_1, sequence_1 in sequence_dictonary:
	for name_2, sequence_2 in sequence_dictonary:
		if name_1 != name_2 and sequence_1[-3:] == sequence_2[0:3]:
		   print name_1 ,name_2     
    		
				

