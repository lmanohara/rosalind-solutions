"""
Complementing a Strand of DNA
"""
import fileinput

for dna in fileinput.input("rosalind_revc.txt"):
	reverse_dna = list(dna) 	
	reverse_dna = reverse_dna[::-1]
	reverse_dna.remove("\n")
	new_reverse_dna = ""	
	print(reverse_dna)
	for x in xrange(len(reverse_dna)):
		component = reverse_dna[0]
		complement = ""
		if component == "A":
			complement = "T"
			del reverse_dna[0]		
		elif component == "T":
			complement = "A"
			del reverse_dna[0]
		elif component == "C":
			complement = "G"
			del reverse_dna[0]
		elif component == "G":
			complement = "C"
			del reverse_dna[0]
		
		new_reverse_dna += complement
	
	print(new_reverse_dna)
