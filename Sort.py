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


def selection_sort(array):
    pass


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


if __name__ == '__main__':
    l = [5, 2, 3, 6, 1, 0, 4]
    print(l)
    print(bubble_sort(l))
    print(insertion_sort(l))
