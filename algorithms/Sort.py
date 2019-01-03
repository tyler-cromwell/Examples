#!/usr/bin/env python3

def bubble_sort(data):
    array = data[:]

    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[j-1] > array[j]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp

    return array


def selection_sort(data):
    array = data[:]

    for j in range(len(array)-1):
        iMin = j

        for i in range(j+1, len(array)):
            if array[i] < array[iMin]:
                iMin = i

        if iMin != j:
            temp = array[iMin]
            array[iMin] = array[j]
            array[j] = temp

    return array


def insertion_sort(data):
    array = data[:]
    i = 1

    while i < len(array):
        j = i

        while j > 0 and array[j-1] > array[j]:
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
            j -= 1

        i += 1

    return array


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
    l = [5, 2, 3, 6, 1, 0, 4]
    print('Unordered:\t', l)
    print('Bubble Sort:\t', bubble_sort(l))
    print('Selection Sort:\t', selection_sort(l))
    print('Insertion Sort:\t', insertion_sort(l))
    print('Merge Sort:\t', merge_sort(l))
