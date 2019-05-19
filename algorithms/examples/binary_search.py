#!/usr/bin/env python3

import random
import sys

sys.path.append('..')
import divide_and_conquer as dc


if __name__ == '__main__':
    print('====================')
    print('Binary Search')
    print('====================')

    s = 10
    l = [random.randint(0, s) for i in range(s)]

    print('Original:', l)
    l.sort()
    print('Sorted:', l)

    for e in l:
        r = random.randint(0, s)
        print('Searching for', r, ':', dc.binary_search(l, r))
