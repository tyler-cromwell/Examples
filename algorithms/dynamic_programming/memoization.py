#!/usr/bin/env python3

##################################################
#  Method: Memoization
#
#  Status: COMPLETE
#  TODO: Add stack overflow exception handling
##################################################

import getopt
import sys


def step(A, n):
    if A[n] != 0:
        # Use saved value
        return A[n]
    elif n < 0:
        # Invalid step, exclude
        return 0
    elif n == 0:
        # Valid step, include
        return 1
    else:
        # Keep jumping and save
        A[n] = step(A, n-1) + step(A, n-2) + step(A, n-3)
        return A[n]


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

        A = [0] * (n+1)
        print('{}'.format(step(A, n)))
