#!/usr/bin/env python3
sequences = open('rosalind_hamm.txt').readlines()
seqs = [line.strip() for line in sequences]
print(seqs)
# print(sum(1 for a,b in zip(seqs[0],seqs[1]) if a!=b))