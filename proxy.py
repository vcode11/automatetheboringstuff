import os
import sys
from getpass import getpass

def set_proxy():
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
    os.system('git config --global http.proxy http://{username}:{password}@{address}:{port}')
    os.system('git config --global https.proxy https://{username}:{password}@{address}:{port}')

    #For environment variables
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

def unset_proxy():
    files = ['/etc/apt/apt.conf', '/etc/environment', '/etc/default/docker', '/etc/systemd/docker.service.d/http-proxy.conf']
    for file_ in files:
        try:
            with open(file_) as f:
                content = f.readlines()
                content = list(filter(lambda s: 'proxy' not in s.lower(), content))
                with open(file_,'w') as f:
                    for line in content:
                        f.write(line)
        except Exception as e:
            pass
    os.system('git config --unset --global http.proxy')
    os.system('git config --unset --global http.proxy')

try:
    if sys.argv[1] == 'set':
        set_proxy()
    elif sys.argv[1] == 'unset':
        unset_proxy()
except Exception as e:
    print('Usage: sudo python3 proxy.py set # Sets Proxy for terminal')
    print('sudo python3 unset_proxy.py unset # Unsets Proxy for terminal')
