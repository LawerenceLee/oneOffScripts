#!/usr/bin/python
'''Script makes python programs executable at the
terminal by simply typing their name.

Author: Zach Owens
Created: Friday Oct 13, 2017
'''
import os
import sys

CWD_CONTENTS = os.listdir(os.getcwd())


def main(filename):
    '''Changes filename's permissions so all users may execute it,
    copys file to /usr/local/bin, and drops its file extension in
    the process.'''

    if filename in CWD_CONTENTS:
        os.system('chmod +x {}'.format(filename))
        os.system('cp {} /usr/local/bin/{}'.format(filename, filename[:-3]))
        print('\n[+] The {} executable was successfully created\n'.format(
                                                            filename[:-3]))
    else:
        print('[-] The file was not found in the current directory\n')


if __name__ == "__main__":
    '''Clear screen, grab argument after executable if there is one,
    try raw_input of py2.7 if that doesn't work, if that fails just
    use input from py3.6'''

    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        filename = sys.argv[1]
    except IndexError:
        try:
            filename = raw_input("Enter filename with its extension: ")
        except NameError:
            filename = input("Enter filename with its extension: ")
    finally:
        main(filename)
