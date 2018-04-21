#!/usr/bin/python
'''Automates the process of creating Local Git Repositories'''

import os


def git_process():
    try:
        os.system("git init")
        os.system("git add .")
        os.system("git commit -m 'inital commit'")
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
