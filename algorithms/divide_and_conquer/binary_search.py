#!/usr/bin/env python3

import random


def binary_search(sl, data):
    start = 0
    mid = len(sl) // 2
    end = len(sl)

    while end >= start:
        if data > sl[mid]:
            start = mid+1
        elif data < sl[mid]:
            end = mid-1
        else:
            return mid

        mid = ((end - start) // 2) + start

    return -1


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
        print('Searching for', r, ':', binary_search(l, r))
