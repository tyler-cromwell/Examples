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


def _partition(array, start, end):
    pivot = end
    i = start

    print('pivot = {} = array[{}]'.format(array[pivot], end))
    for j in range(start, end):
        if array[j] <= array[pivot]:
            print('swap', array[i], array[j])
            array[i], array[j] = array[j], array[i]
            i += 1

    print('swap', array[i], array[pivot])
    array[i], array[pivot] = array[pivot], array[i]
    print(i, array)
    return i

def _quicksort(array, start, end):
    if start < end:
        print('recursion')
        pivot = _partition(array, start, end)
        _quicksort(array, start, pivot - 1)
        _quicksort(array, pivot + 1, end)

def quicksort(array):
    _quicksort(array, 0, len(array)-1)


if __name__ == '__main__':
    l = [5, 2, 3, 6, 1, 0, 4]
    print('Unordered:\t', l)
    print('Bubble Sort:\t', bubble_sort(l))
    print('Selection Sort:\t', selection_sort(l))
    print('Insertion Sort:\t', insertion_sort(l))
    print('Quick Sort:\t', quicksort(l))
