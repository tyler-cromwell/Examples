#!/usr/bin/env python3

import enum
import sys
sys.path.insert(0, '../')

from _common import Node
from data_structures import Queue


class Traversal(enum.Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


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


def breadth_first_search(root):
    queue = Queue.Queue(root)
    visited = []

    while len(queue) > 0:
        node = queue.dequeue()

        if node not in visited:
            visited.append(node.data)

            for child in node.children():
                queue.enqueue(child)

    return visited


if __name__ == '__main__':
    print('====================')
    print('Depth First Search')
    print('====================')

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

    print()
    print('====================')
    print('Breadth First Search')
    print('====================')

    print('Tree:')
    print(root.data)
    print('+', root.left.data)
    print('+--', root.left.left.data)
    print('+--', root.left.right.data)
    print('+', root.right.data)
    print('+--', root.right.left.data)
    print('+--', root.right.right.data)

    visited = breadth_first_search(root)
    print(visited)
