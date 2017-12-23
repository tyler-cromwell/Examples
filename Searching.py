#!/usr/bin/env python3

import enum
import random

from common import Node


class Traversal(enum.Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


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


def depth_first_search(root, traversal=Traversal.INORDER):
    visited = []

    if traversal == Traversal.PREORDER:
        visited.append(root.data)

        if root.left is not None:
            visited += depth_first_search(root.left, traversal)
 
        if root.right is not None:
            visited += depth_first_search(root.right, traversal)
    elif traversal == Traversal.POSTORDER:
        if root.left is not None:
            visited += depth_first_search(root.left, traversal)
 
        if root.right is not None:
            visited += depth_first_search(root.right, traversal)

        visited.append(root.data)
    else:
        if root.left is not None:
            visited += depth_first_search(root.left, traversal)

        visited.append(root.data)

        if root.right is not None:
            visited += depth_first_search(root.right, traversal)

    return visited


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
        print('Searching for', e, ':', binary_search(l, e))

    root = Node.BinaryNode(5,
        left = Node.BinaryNode(3,
            left = Node.BinaryNode(10),
            right = Node.BinaryNode(2)
        ),
        right = Node.BinaryNode(1,
            left = Node.BinaryNode(7),
            right = Node.BinaryNode(9)
        )
    )

    print()
    print('====================')
    print('Depth First Search')
    print('====================')

    print('Tree:')
    print(root.data)
    print('+', root.left.data)
    print('+--', root.left.left.data)
    print('+--', root.left.right.data)
    print('+', root.right.data)
    print('+--', root.right.left.data)
    print('+--', root.right.right.data)

    visited = depth_first_search(root, Traversal.PREORDER)
    print('Preorder:', visited)
    visited = depth_first_search(root, Traversal.POSTORDER)
    print('Postorder:', visited)
    visited = depth_first_search(root)
    print('Inorder:', visited)
