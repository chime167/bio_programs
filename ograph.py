#!/usr/bin/env python3

def main():
    import re
    results = []
    seq = ''
    f = open('rosalind_grph.txt')
    for line in f:
        line = line.rstrip()
        m = re.match('>([\s\S]+)', line)
        if m:
            dic = {'header': m.group(1), 'seq': None}
            seq = ''
            results.append(dic)
        else:
            seq = seq + line
            dic['seq'] = seq 
    
    header = [sub['header'] for sub in results]
    sequence = [sub['seq'] for sub in results]
    
    k = 3
    s = []
    t = []

    for i,y in enumerate(header):
        for j,z in enumerate(sequence):
            if i != j:
                if sequence[i][-k:] == sequence[j][0:k]:
                    s.append(header[i])
                    t.append(header[j])
    
    for x,y in enumerate(s):
        print(s[x], t[x])

            

        

if __name__ == '__main__': main()
 
