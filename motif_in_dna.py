"""
Finding a Motif in DNA
"""
import fileinput

line_list = []

for line in fileinput.input("rosalind_subs.txt"):
	line_list.append(line.strip())

dna_string = line_list[0]
dna_substring = line_list[-1]

#get 1st position and position - length of the substring
for x in range(0, len(dna_string)-len(dna_substring)):
	if dna_string[x] == dna_substring[0]:
		if dna_string[x: x + len(dna_substring)] == dna_substring:
			print x + 1,
		
				

