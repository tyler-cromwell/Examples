import random


def binary_search(sl, data):
    start = 0
    mid = len(sl) // 2
    end = len(sl) - 1

    while end >= start:
        if data > sl[mid]:
            start = mid+1
        elif data < sl[mid]:
            end = mid-1
        else:
            return mid

        mid = ((end - start) // 2) + start

    return -1


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
