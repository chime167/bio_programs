#!/usr/bin/env python3

def main():
    import re
    import itertools
    results = []
    seq = ''
    f = open('aaa.txt')
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
    
    res1 = [sub['header'] for sub in results]
    res2 = [sub['seq'] for sub in results]
    dic2 = {}
    for key, value in zip(res1, res2):
        dic2[key] = value

    
    combinations = itertools.combinations(res2, 2)
    for a, b in combinations:
        if a[-3:] == b[0:3] or b[-3:] == a[0:3]:
            position1 = res2.index(a)
            position2 = res2.index(b)
            print(res1[position1], res1[position2])
            

        

if __name__ == '__main__': main()
