def main():
    print(rcomp(open('rosalind_revc.txt')))


def rcomp(t):
    rc = ''
    for line in t:
        line2 = line.replace('A', 't')
        line3 = line2.replace('G', 'c')
        line4 = line3.replace('C', 'g')
        line5 = line4.replace('T', 'a')
        c = line5.upper()
        rc = c[::-1]
    return rc



if __name__ == '__main__':
    main()
