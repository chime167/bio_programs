#!/usr/bin/env python3
def main():
    print(dna2rna(open('rosalind_rna.txt').read()))


def dna2rna(t):
    u = t.replace('T', 'U')
    return u






if __name__ == '__main__':
    main()