#!/usr/bin/python
'''Automates the process of creating Local Git Repositories'''

import os
from subprocess import Popen
import time


def git_process():
    try:
        Popen(["git", 'init'])
        time.sleep(1)
        Popen(['git', 'add', '*'])
        time.sleep(2)
        Popen(['git', 'commit', '*', '-m', '"inital commit"'])
        time.sleep(2)
    except Exception as e:
        print(e + '\n')
        print('[-] An error occured in the creation of the Git Repository!\n')
    else:
        print('\n[+] Successful creation of the Git Repository\n')


def main():
    git_process()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else "clear")
    main()
