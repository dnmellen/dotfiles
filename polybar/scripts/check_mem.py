#!/usr/bin/python3

import sys
import subprocess


def check_mem_available():
    info = subprocess.run(['free', '--giga'], stdout=subprocess.PIPE).stdout
    mem_info = info.splitlines()[1].split()
    total = mem_info[1].decode()
    used = mem_info[2].decode()
    print(f'MEM {used}GB/{total}GB (used/total)')

if __name__ == '__main__':
    check_mem_available()
