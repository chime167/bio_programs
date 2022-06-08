import re
s = '_hi_'

for i in s:
    m = re.match('_hi_', i)
    if m:
        print('yes')
    else:
        print('no')