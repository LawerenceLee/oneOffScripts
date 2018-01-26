#!/usr/bin/python
'''Scans a specified directory and reports back on the size of each file
within it, as well all files in its parent directories.

Author: Kenneth Love
Edited by: Zach Owens. OCT 11, 2017
'''
import os


def treewalker(start):
    total_size = 0
    total_files = 0

    for root, dirs, files in os.walk(start):
        subtotal = sum(
            os.path.getsize(os.path.join(root, name)) for name in files
        )
        total_size += subtotal
        file_count = len(files)
        total_files += file_count
        print(root, "consumes", subtotal,
              'bytes in', file_count, 'non-directory files')

    print(start, "contains", total_files,
          "files with a combined size of", total_size, "bytes")


if __name__ == "__main__":
    path = input('Enter a Directroy Filepath: ')
    treewalker(path)
