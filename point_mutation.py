#!/usr/bin/env python3
def main():
    count = 0
    with open('rosalind_hamm.txt') as f:
        dna = [line.rstrip() for line in f]
    s1 = dna[0]
    s2 = dna[1]
    for b1, b2 in zip(s1, s2):
        if b1 != b2:
            count = count + 1
    return count
        
        
        



if __name__ == '__main__':
    print(main())