#!/usr/bin/python
'''Activates a python 3.6 virtual environment with
Jupyter Notebooks installed.

WILL ONLY WORK IF YOU NEED TO ACTIVATE A VIRTUAL ENVIRONMENT
WITHIN AN instance of subprocess.Popen

Author: Zach Owens
Date: 10/11/17
'''

import os
from subprocess import Popen


def main():
    '''Runs the command to activate a pre-made python 3.6 virtualenv'''
    try:
        Popen('source /Users/lawerencelee/Environments/py36_env/bin/activate',
              shell=True)
    except Exception as e:
        print('[-] EXCEPTION: \n{}\n'.format(e))
    else:
        print('[+] py36_env ACTIVATED')


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
