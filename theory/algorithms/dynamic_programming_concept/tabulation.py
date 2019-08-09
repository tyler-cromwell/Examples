#!/usr/bin/env python3

##################################################
#  Method: Tabulation
#
#  Status: COMPLETE
##################################################

import getopt
import sys


def step(n):
    prev1 = 1
    prev2 = 0
    prev3 = 0
    result = 0

    for i in range(n):
        result = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = result

    return result


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
