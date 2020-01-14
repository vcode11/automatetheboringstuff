import os
import sys
from getpass import getpass

address = input('Enter the proxy address:')
address = address.strip()
address = '.'.join([w.strip() for w in address.split('.')])
port = int(input('Enter port:'))
username = input('Enter Username:')
password = getpass(prompt='Password:')

#For apt software centre
with open('/etc/apt/apt.conf','w') as f:
    verbs = ['http','https','ftp']
    for verb in verbs:
        f.write(f'Acquire::{verb}::proxy "{verb}://{username}:{password}@{address}:{port}/";\n')
#For docker
os.makedirs('/etc/systemd/system/docker.service.d',exist_ok=True)
os.makedirs('/etc/default/',exist_ok=True)
with open('/etc/systemd/system/docker.service.d/http-proxy.conf','w') as f:
    f.write(f'''[Service]
Environment="HTTP_PROXY=http://{address}:{port}"
Environment="HTTPS_PROXY=http://{address}:{port}"
Environment="NO_PROXY=localhost,127.0.0.1"''')


with open('/etc/default/docker','w') as f:
    f.write(f'''[Service]
Environment="HTTP_PROXY=http://{address}:{port}"
Environment="HTTPS_PROXY=http://{address}:{port}"
Environment="NO_PROXY=localhost,127.0.0.1"''')

#For git etc...
content = []
with open('/etc/environment') as f:
    content = f.readlines()
    content = list(filter(lambda s: 'proxy' not  in s, content))
    with open('/etc/environment','w') as f:
        for line in content:
            f.write(line)
        verbs = ['http','https','ftp']
        for verb in verbs:
            f.write(f'{verb}_proxy={verb}://{username}:{password}@{address}:{port}/\n')
