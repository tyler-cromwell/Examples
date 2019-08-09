#!/usr/bin/env python3

##################################################
#  Method: Naive
#
#  Status: COMPLETE
#  TODO: Add stack overflow exception handling
##################################################

import getopt
import sys


def step(n):
    if n < 0:
        # Invalid step, exclude
        return 0
    elif n == 0:
        # Valid step, include
        return 1
    else:
        # Keep jumping
        return step(n-1) + step(n-2) + step(n-3)


if __name__ == '__main__':
    try:
        short_opts = 'n:'
        long_opts = ['help', 'n=']
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError as error:
        print('Invalid argument: \"{}\"\n'.format(str(error)))
        print('Please specify the number of steps (-n)')

    if len(opts) == 0:
        print('Please specify the number of steps (-n)')
    else:
        n = 0

        for o, a in opts:
            if o == '-n' or o == '--n':
                n = int(a)

        print('{}'.format(step(n)))
