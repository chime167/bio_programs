#!/usr/bin/env python3
import re
import argparse

    
def main():
    '''Program that finds all instances of a substring in a DNA sequence.
    CLI parameters:
        filename: the file containing the DNA sequence.
        motif: the substring you want to look for
    The program provides the indexes at which the substring begins
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Enter the filename or path to file')
    parser.add_argument('motif', help='Enter the motif to be searched for')
    args = parser.parse_args()

    #open file and convert each strand into a list
    with open(args.filename) as f:
        s = ''.join([line.rstrip() for line in f])
    #converts list items to strings and removes newline char
    t = args.motif

    #this regex finds all occurences of pattern *including overlap*
    runs = re.finditer(rf'(?={t})', s)
    startlist = [m.start() for m in runs]
    

    #converts list of starts to space separated string
    #map applies the str function to each element
    starts = ' '.join(map(str, startlist))
    print(starts)
if __name__ == '__main__': main()