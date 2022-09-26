#!/usr/bin/python3

import sys
import json
import subprocess

def check_cpu_temp():
    info = json.loads(subprocess.run(['sensors', '-j'], stdout=subprocess.PIPE).stdout)
    try:
        cpu_temp = info['k10temp-pci-00c3']['Tctl']['temp1_input']
        print(f'CPU {cpu_temp}°C')
    except Exception:
        print("Cannot get CPU temp")

if __name__ == '__main__':
    check_cpu_temp()
