#!/usr/bin/env python3
def main():
    count = 0
    dna = []
    f = open('rosalind_hamm.txt')
    for line in f:
        dna.append(line.rstrip())
    s1 = dna[0]
    s2 = dna[1]
    for b1, b2 in zip(s1, s2):
        if b1 != b2:
            count = count + 1
    return count
        
        
        



if __name__ == '__main__':
    print(main())