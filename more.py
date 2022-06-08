def main():
    print(dna2rna(open('rosalind_rna.txt')))


def dna2rna(t):
    u = ''
    for line in t:
        line = line.replace('T', 'U')
        u = u + line
    return u



if __name__ == '__main__':
    main()


