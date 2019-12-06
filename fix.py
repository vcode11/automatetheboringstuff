'''Filename:fix.py 
 Usage:To justify content of a text file at 72 characters per line
       python3 fix.py <file-to-be-justified> 
       I wrote this just as a simple exercise. 
       I had to format a large number of text files so I wrote this script.
'''
import sys, os
def justify(s):
    l = s.split('\n')
    #print(l)
    for i in range(len(l)-1):
        l[i] = l[i].rstrip()
        if len(l[i]) >= 75:
            idx = (l[i][:75]).rfind(' ')
            l[i+1] = l[i][idx+1:] + ' ' + l[i+1]
            l[i] = l[i][:idx]
    while len(l[-1]) >= 75:
        l.append('')
        idx = (l[-2][:75]).rfind(' ')
        l[-1] = l[-2][idx+1:]
        l[-2] = l[-2][:idx]
    justified_text = '\n'.join(l)
    return justified_text
            
try:
    filename = sys.argv[1]
except Exception as e:
    print(e)
    sys.exit(0)
content = ''
with open(filename) as f:
    content = f.read()
content = justify(content)
with open(filename, 'w') as f:
    f.write(content)


