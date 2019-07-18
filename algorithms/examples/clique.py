#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/'+ os.pardir +'/')
from algorithms import graph


# Graph representation
N = [
    [1, 2, 3, 5, 7],
    [0, 2, 4, 6],
    [0, 1, 3, 4],
    [0, 2, 4, 5, 6, 7],
    [1, 2, 3, 5, 6, 8],
    [0, 3, 4, 6, 7],
    [1, 3, 4, 5, 8],
    [0, 3, 5],
    [4, 6]
]

# Vertex set
V = []

# Edge set
E = []


if __name__ == '__main__':
    print('====================')
    print('Clique')
    print('====================')

    for v in range(len(N)):
        V.append(v)

    for v in range(len(N)):
        for n in N[v]:
            E.append((v, n))

    print(graph.clique(V, E, k=4))
