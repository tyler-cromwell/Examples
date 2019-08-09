#!/usr/bin/env python3

import divide_and_conquer as dc


"""
Sort A1 according to the order defined by A2.
"""
def relative_sort(A1, A2):
    """
    1) Copy A1 as temp and sort it
    2) Create an array to track visits
    """
    m = len(A1)
    n = len(A2)
    visited = [0] * m
    temp = A1.copy()
    temp.sort()
    index = 0     # for index of output which is sorted A1[]

    """
    (3) For all elements of A2:
    """
    for i in range(0, n):
        """
        (3.1) Find the first occurrence in temp, skip if not found
        """
        f = dc.binary_search_first(temp, A2[i])
        if f == -1: continue

        """
        (3.2) Copy all occurrences into A1
        """
        j = f
        while j < m and temp[j] == A2[i]:
            A1[index] = temp[j]
            index = index+1
            visited[j] = 1
            j = j+1

    """
    (4) Copy all remaining elements of temp onto the end of A1
    """
    for i in range(0, m):
        if visited[i] == 0:
            A1[index] = temp[i]
            index = index+1


if __name__ == '__main__':
    A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    A2 = [2, 1, 8, 3, 10]
    relative_sort(A1, A2)
    print("Sorted array is:", A1, '<=>', A2)
