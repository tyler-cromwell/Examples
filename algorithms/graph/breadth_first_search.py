#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../')

from _common import Node
from data_structures import Queue


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
    print('Breadth First Search')
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

    visited = breadth_first_search(root)
    print(visited)
