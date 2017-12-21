#!/usr/bin/env python3

import random


def binary_search(sl, data):
    start = 0
    mid = len(sl) // 2
    end = len(sl)

    while end != start:
        if data > sl[mid]:
            start = mid
        elif data < sl[mid]:
            end = mid
        else:
            return mid

        mid = ((end - start) // 2) + start

    return -1


if __name__ == '__main__':
    s = 20
    l = [random.randint(0, s) for i in range(s)]

    print(l)
    l.sort()
    print(l)

    for e in l:
        print('Searching for', e, ':', binary_search(l, e))
