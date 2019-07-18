#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/'+ os.pardir +'/')
from algorithms import dynamic_programming as dp


if __name__ == '__main__':
    s1 = 'ABAB'
    s2 = 'BABA'
    s3 = 'ABAB'
    s4 = 'ABBA'
    s5 = 'BBB'

    lcsu1 = dp.longest_common_substring(s1, s2)
    lcsu2 = dp.longest_common_substring(s1, s3)
    lcsu3 = dp.longest_common_substring(s4, s3)
    lcsu4 = dp.longest_common_substring(s1, s5)

    print(lcsu1, 'in lcsu({}, {})'.format(s1, s2))
    print(lcsu2, 'in lcsu({}, {})'.format(s1, s3))
    print(lcsu3, 'in lcsu({}, {})'.format(s4, s3))
    print(lcsu4, 'in lcsu({}, {})'.format(s1, s5))
