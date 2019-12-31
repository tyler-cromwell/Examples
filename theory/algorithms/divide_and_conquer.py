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
Sorts the given array 'A'.
"""
def quick_sort(A):
    def quick_sort_inner(A, l, h):
        n = len(A)

        if (n == 1) or (n == 2 and A[0] <= A[1]):
            return A
        elif n == 2 and A[0] > A[1]:
            return [A[1], A[0]]

        if l < h:
            pivot = A[h]
            i = l

            for j in range(l, h):
                if A[j] < pivot:
                    temp = A[j]
                    A[j] = A[i]
                    A[i] = temp
                    i += 1

            temp = A[h]
            A[h] = A[i]
            A[i] = temp

            quick_sort_inner(A, l, i-1)
            quick_sort_inner(A, i+1, h)

    return quick_sort_inner(A, 0, len(A)-1)


"""
Function aliases.
"""
bs = binary_search
bsf = binary_search_first
ms = merge_sort
qs = quick_sort
