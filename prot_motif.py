#!/usr/bin/env python3
import requests
import re
import argparse


def main():
    pattern = re.compile(r'(?=N[^P][ST][^P])')
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Enter the filename or path to file')
    args = parser.parse_args()
    with open(args.filename) as f:
        names = [line.rstrip() for line in f]
    for name in names:
        identifier = name.split('_')[0]
        request = requests.get(f'http://www.uniprot.org/uniprot/{identifier}.fasta')
        entry = request.text.strip().splitlines()
        seq = ''
        for line in entry:
            line = line.rstrip()
            if re.match(r'>.+', line):
                seq = ''
            else:
                seq += line
                starts = [m.start()+1 for m in re.finditer(pattern, seq)]
        
        if starts:
            print(name)
            print(*starts)
                
                
if __name__ == '__main__': main()

        
    
    