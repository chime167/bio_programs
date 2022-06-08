import re

# def main():
#     print(gccontent(open('test.txt')))

def main():
    seq = ''
    keys = []
    values = []
    dic = {}
    for line in open('test.txt'):
        m = re.match(r'>([\s\S]+)', line.rstrip())
        if m:
            seq = ''
            keys.append(m.group(1))
        else:
            seq = seq + line.rstrip()
            values.append(seq)
    for key, value in zip(keys, values):
        dic[key] = value
      
    dic2 = {k:getgc(v) for k, v in dic.items()}
    maxk = max(dic2, key=dic2.get)
    maxv = max(dic2.values())
    return f'{maxk}\n{maxv}'
    
def getgc(x):
    gcontent = x.count('G')
    ccontent = x.count('C')
    gc = ((gcontent + ccontent) / len(x)) * 100
    return gc



         
    
            
if __name__ == '__main__':
    print(main())


    
        
    
            
if __name__ == '__main__':
    main()
