#!/usr/bin/env python3
import argparse
import re


def main():
    '''Program that finds the longest common substring between a set of DNA sequences.
    CLI parameters:
        filename: the FASTA file or FASTA style file to pass to the program
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Enter the filename or path to file')
    args = parser.parse_args()
    lis = []
    with open(args.filename) as file:
        for line in file:
            line = line.rstrip()
            #regex where group 1 matches the ID
            m = re.match(r'>([\s\S]+)', line)
            if m:
                #makes a dict to store 2 fields of interest
                dic = {'name': m.group(1), 'seq': None}
                #ensures the seq variable is emptied for each match in the file
                seq = ''
                lis.append(dic)
            else:
                #populates the seq variable before updating the dictionary
                seq += line
                dic['seq'] = seq
    return lis


def find_longest_sub(lst_of_dicts):
    #this turns the list of dicts into lists of keys and values of interest
    sequence = [sub['seq'] for sub in lst_of_dicts]
    shortest = sorted(sequence, key=len)[0]

    r = len(shortest)

    for _ in range(r - 1):
        r -= 1
        for i in range(len(shortest) - r):
            motif = shortest[i:i+r]
            if all(seq.find(motif) >= 0 for seq in sequence):
                return motif
            # full_match = [m for m in motif if all(m in seq for seq in sequence)]
            # if full_match:
            #     return full_match[0]



if __name__ == '__main__':
    print(find_longest_sub(main()))
