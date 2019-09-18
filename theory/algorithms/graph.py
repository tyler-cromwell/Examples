#!/usr/bin/env python3

import itertools
import sys

sys.path.append('../../')
from data_structures import Queue, Stack


def breadth_first_search(root):
    queue = Queue.Queue(root)
    visited = []

    while len(queue) > 0:
        node = queue.dequeue()

        if node.data not in visited:
            visited.append(node.data)   # .data acts as a unique identifier

            for child in node.children():
                queue.enqueue(child)

    return visited


def clique(V, E, k):
    count = 0
    clique = []

    for group in list(itertools.combinations(V, k)):
        edges = list(itertools.combinations(group, 2))
        n = len(edges)

        for edge in edges:
            if edge in E:
                count += 1

        if count == n:
            clique.append(group)
            return True, clique
        else:
            count = 0
            clique = []

    return False, clique


def depth_first_search(root):
    stack = Stack.Stack(data=root)
    visited = []

    while len(stack) > 0:
        node = stack.pop()

        if node.data not in visited:
            visited.append(node.data)   # .data acts as a unique identifier

            for child in node.children():
                stack.push(child)

    return visited


"""
Function aliases.
"""
bfs = breadth_first_search
dfs = depth_first_search
