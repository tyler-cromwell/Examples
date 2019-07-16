import random

"""
Searches for 'data' in the given 'array'.
"""
def binary_search(A, data):
    low = 0
    mid = len(A) // 2
    high = len(A) - 1

    while high >= low:
        if data > A[mid]:
            low = mid+1
        elif data < A[mid]:
            high = mid-1
        else:
            return mid

        mid = (high + low) // 2

    return -1


"""
Variant of traditional Binary Search to find
the first occurrence of a number.
"""
def binary_search_first(A, number):
    high = len(A)-1
    low = 0

    while high >= low:
        mid = (low + high) // 2
        if number == A[low]:
            return low
        elif number > A[low] and number <= A[mid]:
            high = mid
            low = low +1
        elif number >= A[mid] and number <= A[high]:
            low = mid
        elif number < A[low] or number > A[high]:
            return -1

    return -1


"""
Sorts the given array 'A'.
"""
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


"""
Function aliases.
"""
bs = binary_search
bsf = binary_search_first
ms = merge_sort
