#!/usr/bin/env python3

"""
tarball-pathlengths.py - show the twenty largest path lengths in tarball
Usage: %(prog)s <tarball>

This is quite useful for finding out where to shave off a few characters
in the file name length if you are being hit by the 99 character limit
for file names in some (older) tar file formats.
"""

# sort(1) cannot sort by line length, so we are doing this in Python.
#
# Python3's tarball module supports lzma/xz compression, so we have
# switched from Python2 to Python3.

import sys
import tarfile

def check_tarfile(filename, fileobj):
    tar = tarfile.open(fileobj=fileobj)
    fnames = tar.getnames()
    fnames.sort(key=lambda x: len(x),
                reverse=True)
    # print(filename)
    for fname in fnames[:20]:
        print("%3d %s" % (len(fname), fname))
    tar.close()

def main(args):
    # When no command line arguments are given, read tar file from stdin
    if args == []:
        args = ['-']

    for filename in args:
        if filename == '-':
            check_tarfile('stdin', sys.stdin.buffer)
        else:
            with open(filename, 'rb') as fileobj:
                check_tarfile(filename, fileobj)

if __name__ == '__main__':
    main(sys.argv[1:])
