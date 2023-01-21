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
    result_dict = {}
    current_header = None
    with open(args.filename) as file:
        for line in file:
            line = line.rstrip()
            #regex where group 1 matches the ID
            m = re.match(r'>([\s\S]+)', line)
            if m:
                current_header = m.group(1)
                result_dict[current_header] = ''
            else:
                result_dict[current_header] += line

    return result_dict


def find_longest_sub(dicts):
    sequence = dicts.values()
    shortest = min(sequence, key=len)

    outer_loop = len(shortest)
    inner_loop = outer_loop

    for _ in range(outer_loop - 1):
        outer_loop -= 1
        for i in range(inner_loop - outer_loop):
            motif = shortest[i:i+outer_loop]
            if all(motif in seq for seq in sequence):
                return motif
            # full_match = [m for m in motif if all(m in seq for seq in sequence)]
            # if full_match:
            #     return full_match[0]



if __name__ == '__main__':
    print(find_longest_sub(main()))
