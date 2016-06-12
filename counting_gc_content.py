"""
Computing GC Content
"""
from Bio import SeqIO

def computeContent(sequence):
    Ccount = sequence.count("C")
    GCount = sequence.count("G")
    CGPersentage = (float(Ccount + GCount) / float(len(sequence))) * 100
    return CGPersentage 

file = open("rosalind_gc.fasta")
fasta_sequences = SeqIO.parse(file,'fasta')
persentages = []
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)
    persentages.append(computeContent(sequence))
    

print(max(persentages)) 
	
