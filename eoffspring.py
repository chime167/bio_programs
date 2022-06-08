#!/usr/bin/env python3

def main():
    dat = open('rosalind_iev.txt')
    for number in dat:
        number = number.rstrip()
        numbers = number.split(' ')
        numbers = [int(x) for x in numbers]
    print(expected_offspring(*numbers))


def expected_offspring(AAAA,AAAa,AAaa,AaAa,Aaaa,aaaa):
    p1 = 1
    p2 = 1
    p3 = 1
    p4 = (3/4)
    p5 = (1/2)
    p6 = 0
    prob = (2*AAAA)*p1+(2*AAAa)*p2+(2*AAaa)*p3+(2*AaAa)*p4+(2*Aaaa)*p5+(2*aaaa)*p6
    return prob

if __name__ == '__main__': main()