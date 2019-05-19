#!/usr/bin/env python3

import random


def merge_sort(A):
    def merge(L, R):
        B = []

        while len(L) != 0 and len(R) != 0:
            if L[0] < R[0]:
                B.append(L[0])
                L.remove(L[0])
            else:
                B.append(R[0])
                R.remove(R[0])

        if len(L) == 0:
            B.extend(R)
        else:
            B.extend(L)

        return B

    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        L = merge_sort(A[:mid])
        R = merge_sort(A[mid:])
        return merge(L, R)


if __name__ == '__main__':
    print('====================')
    print('Merge Sort')
    print('====================')

    l = [random.randint(0, 100) for i in range(10)]
    print('Unordered:\t', l)
    print('Merge Sort:\t', merge_sort(l))
