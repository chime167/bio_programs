#!/usr/bin/env python3


def main():
    import re
    from difflib import SequenceMatcher
    f = open('deletethis.txt')
    lis = []
    seq = ''
    for line in f:
        #regex where group 1 matches the ID
        m = re.match(r'>([\s\S]+)', line.rstrip())
        if m:
            #makes a dict to store 2 fields of interest
            dic = {'name': m.group(1), 'seq': None}
            #ensures the seq variable is emptied for each match in the file
            seq = ''
            lis.append(dic)
        else:
            #populates the seq variable before updating the dictionary
            seq = seq + line.rstrip()
            dic['seq'] = seq
   
    #this turns the list of dicts into lists of keys and values of interest
    res = [sub['name'] for sub in lis]
    res2 = [sub['seq'] for sub in lis]

    def shortest(lst):
        



if __name__ == '__main__': main()