#!/usr/bin/env python3
def main():
    import re
    import argparse
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
    startlist = [(m.start() + 1) for m in runs]
    #+1 bc Python starts at 0 - Rosalind example starts at 1

    #converts list of starts to space separated string
    #map applies the str function to each element
    starts = ' '.join(map(str, startlist))
    print(starts)
    results = [(str(match.group(1))) for match in runs]
    #print(results)
if __name__ == '__main__': main()