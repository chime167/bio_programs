s = open('rosalind_dna.txt')
r = s.read()

print(r.count('A'), r.count('C'), r.count('G'), r.count('T'))