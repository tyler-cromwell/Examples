#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/'+ os.pardir +'/')
from data_structures.node import BinaryNode
from algorithms import graph


if __name__ == '__main__':
    print('====================')
    print('Breadth First Search')
    print('====================')

    root = BinaryNode(5,
        left = BinaryNode(3,
            left = BinaryNode(10),
            right = BinaryNode(2)
        ),
        right = BinaryNode(1,
            left = BinaryNode(7),
            right = BinaryNode(9)
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
