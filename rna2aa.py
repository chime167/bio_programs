def main():
    f = open('rosalind_prot.txt')
    r = f.read().rstrip()
    print(rna2aa(r))
#!/usr/bin/env python3
def rna2aa(rna):
    gencode = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
 'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
 'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
 'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
 'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
 'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
 'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
 'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
 'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
 'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
 'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'
     }
    aa = ''
    last_codon_start = len(rna) - 2
    for rf in range(0, last_codon_start, 3):
        codon = rna[rf:rf+3]
        aa += gencode[codon]
    return aa

        
        
if __name__ == '__main__': main()