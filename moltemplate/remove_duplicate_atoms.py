#!/usr/bin/env python3

# Author: Andrew Jewett (jewett.aij at g mail)
# License: MIT License  (See LICENSE.md)
# Copyright (c) 2013

"""
   Get rid of lines containing duplicate copies of the same atom in the "Atoms"
   section of a LAMMPS data file.  Duplicate lines which occur later are
   preserved and the earlier lines are erased.
   The file is read from sys.stdin.  This program does not parse the entire
   data file.  The text from the "Atoms" section of the LAMMPS file must
   be extracted in advance before it is sent to this program.)

"""

import sys

try:
    from .ttree_lex import SplitQuotedString
except (ImportError, SystemError, ValueError):
    # not installed as a package
    from ttree_lex import SplitQuotedString

def main():
    in_stream = sys.stdin
    f = None
    fname = None
    if len(sys.argv) == 2:
        fname = sys.argv[1]
        f = open(fname, 'r')
        in_stream = f

    atom_ids_in_use = set([])

    lines = in_stream.readlines()

    # Start at the end of the file and read backwards.
    # If duplicate lines exist, eliminate the ones that occur earlier in the file.
    i = len(lines)
    while i > 0:
        i -= 1
        line_orig = lines[i]
        line = line_orig.rstrip('\n')
        if '#' in line_orig:
            ic = line.find('#')
            line = line_orig[:ic]

        # Split the line into words (tokens) using whitespace delimeters
        tokens = SplitQuotedString(line,
                                   quotes='{',
                                   endquote='}')

        if len(tokens) > 0:
            atom_id = tokens[0]
            if atom_id in atom_ids_in_use:
                del lines[i]
            else:
                atom_ids_in_use.add(atom_id)
        else:
            del lines[i]


    for line in lines:
        sys.stdout.write(line)

    if f != None:
        f.close()

    return


if __name__ == '__main__':
    main()
