#!/usr/bin/env python3

def main():
    import re
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Enter the filename or path to file')
    parser.add_argument('overlap', help='Enter the length of the overlap e.g. 3 for AGT AGT')
    args = parser.parse_args()
    results = []
    seq = ''
    with open(args.filename) as f:
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
    
    k = int(args.overlap)
    s = []
    t = []
    first_half = []
    second_half = []

    for i, _ in enumerate(header):
        for j, _ in enumerate(sequence):
            if i != j:
                if sequence[i][-k:] == sequence[j][0:k]:
                    s.append(header[i])
                    t.append(header[j])
                    first_half.append(sequence[i])
                    second_half.append(sequence[j])
    
    # for x, y in zip(s, t):
    #     print(x, y)
    for x, y in zip(first_half, second_half):
        print(x + y[k:] + '\n')

            

        

if __name__ == '__main__': main()
 
