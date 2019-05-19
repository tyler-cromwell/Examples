#!/usr/bin/env python3

import sys

sys.path.append('../')
sys.path.append('../../')
from _common import Node
import graph


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

    visited = graph.breadth_first_search(root)
    print(visited)
