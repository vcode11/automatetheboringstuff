''' Filename: set_proxy.py 
 Author: Vishal Mishra
 Purpose: Sets a proxy in Ubuntu
 Usage: sudo python3 set_proxy.py
 '''
import os
from getpass import getpass

address = input('Enter the proxy address:')
address = address.strip()
address = '.'.join([w.strip() for w in address.split('.')])
port = int(input('Enter port:'))
username = input('Enter Username:')
password = getpass(prompt='Password:')

os.chdir('/etc/apt/')
with open('apt.conf','w') as f:
    verbs = ['http','https','ftp']
    for verb in verbs:
        f.write(f'Acquire::{verb}::proxy "{verb}://{username}:{password}@{address}:{port}/";\n')
