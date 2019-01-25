#! /usr/bin/env python3
import shelve
import pyperclip
import sys
if len(sys.argv) == 1:
    print(''' Usage:
            ./mcb.pyw list
                This will list all saved keywords.
            ./mcb.pyw save <keyword>
                This will save clipboard's content in keyword
            ./mcb.pyw <keyword>
                this will copy keywords content to clipboard
            ''')
    sys.exit(0)
mcb = shelve.open('mcbData')
if sys.argv[1] == 'list' or sys.argv[1] == 'l':
    for key in mcb.keys():
        print(key)
    sys.exit(0)
if sys.argv[1] == 'save' or sys.argv[1] == 's':
    mcb[sys.argv[2]] = pyperclip.paste()
else:
    if sys.argv[1] in mcb.keys():
        pyperclip.copy(mcb[sys.argv[1]])
    else: 
        print('No such keyword use list command to see all available keywords.')
mcb.close()
