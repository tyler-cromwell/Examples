#!/usr/bin/env python3

import os
import random
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/'+ os.pardir +'/')
from algorithms import divide_and_conquer as dc


if __name__ == '__main__':
    print('====================')
    print('Merge Sort')
    print('====================')

    l = [random.randint(0, 100) for i in range(10)]
    print('Unordered:\t', l)
    print('Merge Sort:\t', dc.merge_sort(l))
