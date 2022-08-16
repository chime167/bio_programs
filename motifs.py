#!/usr/bin/env python3
def main():
    import re

    #open file and convert each strand into a list
    f = open('rosalind_subs.txt')
    strands = f.readlines()
    #converts list items to strings and removes newline char
    s = strands[0].rstrip()
    t = strands[1].rstrip()

    startlist = []
    #this regex finds all occurences of pattern *including overlap*
    runs = re.finditer(rf'(?={t})', s)
    for m in runs:
        #+1 bc Python starts at 0 - Rosalind example starts at 1
        startlist.append((m.start()+1))
        # print(m.end()-1)

    #converts list of starts to space separated string
    #map applies the str function to each element
    starts = ' '.join(map(str, startlist))
    print(starts)
    results = [(str(match.group(1))) for match in runs]
    #print(results)
if __name__ == '__main__': main()