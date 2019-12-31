#!/usr/bin/env python3

import getopt
import sys


if __name__ == "__main__":
    long_options = ['verbose', 'none', 'required=', 'no-short']
    verbose = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "vnr:", long_options)
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for o, a in opts:
        if o in ('-v', '--verbose'):            verbose = True
        elif o in ('-n', '--none'):             print('option -n')
        elif o in ('-r', '--required'):         print('option -r with value,', a)
        elif o in ('--no-short'):               print('option --no-short')
        else:                                   assert False, "unhandled option"

    if verbose:
        print('WORDS!')
