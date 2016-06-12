"""
Find Hamming distance between s and t 
"""
import fileinput

hammingDistange = 0;
dnaStrings = []
for dna in fileinput.input("rosalind_hamm.txt"):
	dnaStrings.append(dna.strip('\n'))

#compaire two dna string to find different elements 
for x in range(len(dnaStrings[0])):
	if dnaStrings[0][x] != dnaStrings[1][x]:
		hammingDistange += 1

print(hammingDistange)	  


