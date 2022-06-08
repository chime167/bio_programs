#!/usr/bin/env python3
from Bio.Seq import Seq

f = open('rosalind_prot.txt')
r = f.read().rstrip()
my_rna = Seq(r)

my_aa = my_rna.translate()

print(my_aa)