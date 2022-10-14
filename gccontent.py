#!/usr/bin/env python3
import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Enter the filename or path to file')
    args = parser.parse_args()
    with open(args.filename) as f:
        lis = []
        
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
        names = [sub['name'] for sub in lis]
        sequences = [sub['seq'] for sub in lis]
    
        #finally another dict is made to combine the keys and values
        dic2 = {}
        for key, value in zip(names, sequences):
            dic2[key] = getgc(value)
        
        #filters for the highest value and key with the highest value
        maxk = max(dic2, key=dic2.get)
        maxv = max(dic2.values())
        # return f'{maxk}\n{maxv}'
        return lis['name']
        
    
def getgc(x):
    gcontent = x.count('G')
    ccontent = x.count('C')
    gc = ((gcontent + ccontent) / len(x)) * 100
    return gc       
    
            
if __name__ == '__main__':
    print(main())

    
