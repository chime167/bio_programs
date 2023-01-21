#!/usr/bin/env python3
import re
from itertools import combinations
import argparse


def main():
    '''This program connects the overlap between the end of 1 DNA strand with the beginning of another.
    CLI parameters:
        filename: the FASTA file or FASTA style file to pass to the program
        overlap: the length of the overlap with which you wish to search the strands
                    (e.g. 3 would connect AACGT with CGTGG)
    The program outputs the two headers or identifers that were matched followed by
    a concatenated DNA strand of the two strands that overlapped, removing the duplicate part.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Enter the filename or path to file')
    parser.add_argument('overlap', help='Enter the length of the overlap e.g. 3 for AGT AGT')
    args = parser.parse_args()
    result_dict = {}
    current_header = None
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip()
            m = re.match('>([\s\S]+)', line)
            if m:
                current_header = m.group(1)
                result_dict[current_header] = ''
            else:
                result_dict[current_header] += line
    
    k = int(args.overlap)
    sequence_pair = []
    id_pair = []


    for pair in combinations(result_dict.values(), 2):
        s1 = pair[0]
        s2 = pair[1]
        fingerprint_s1 = hash(s1[-k:])
        fingerprint_s2 = hash(s2[:k])
        fingerprint3 = hash(s1[:k])
        fingerprint4 = hash(s2[-k:])
        if fingerprint_s1 == fingerprint_s2:
            id_1 = ''.join([k for k, v in result_dict.items() if v == s1])
            id_2 = ''.join([k for k, v in result_dict.items() if v == s2])
            id_pair.append(id_1 + ' ' + id_2)
            sequence_pair.append(s1 + s2[k:])
        elif fingerprint3 == fingerprint4:
            id_1 = ''.join([k for k, v in result_dict.items() if v == s2])
            id_2 = ''.join([k for k, v in result_dict.items() if v == s1])
            id_pair.append(id_1 + ' ' + id_2)
            sequence_pair.append(s2 + s1[k:])
    
    

    for x, y in zip(id_pair, sequence_pair):
        print(x, y, '\n')

            

        

if __name__ == '__main__': main()
