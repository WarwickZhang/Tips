#! /usr/bin/env python

import socket
import os
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

dirpath = os.path.dirname(__file__) + '/'

fopen = open(dirpath + 'chls_base.pac','r')
lines = fopen.readlines()
lines[0] = lines[0].replace("<ipaddress>",get_host_ip())
fopen.close()

tmpPath = dirpath + 'chls.pac'

fopen = open(tmpPath, 'w+')
fopen.writelines(lines)
fopen.close()

os.system('scp ' + tmpPath + ' root@<your-remote-address>:~/pac')
