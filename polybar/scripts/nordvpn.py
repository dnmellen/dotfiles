#!/usr/bin/python3

import sys
import subprocess


def check_nordvpn_status():
    info = subprocess.run(['nordvpn', 'status'], stdout=subprocess.PIPE).stdout
    nordvpn_info = {k.strip(): v.strip() for k, v in [l.split(':') for l in info.decode().splitlines() if 'Status' in l and len(l.split(':')) > 1]}
    status = nordvpn_info['Status']
    if status == 'Connected':
        country = nordvpn_info['Country']
        print(f'NordVPN: Connected ({country})')
    else:
        print(f'NordVPN disconnected')

if __name__ == '__main__':
    check_nordvpn_status()
