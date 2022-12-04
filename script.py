# fly-admin-dhcp и isc-dhcp-server

import subprocess

try:
    packages = subprocess.run('apt list --installed >logfile.txt', shell=True)
    list = open("logfile.txt", "r")
    
    if 'fly-admin-dhcp' and 'isc-dhcp-server' in list.read():
        print('Packages are installed')
    else:
        print('Not found')

finally:
    rm = subprocess.run('rm logfile.txt', shell=True)