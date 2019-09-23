#!/usr/bin/env python3

import itertools
import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/')
from data_structures.Queue import Queue
from data_structures.Stack import Stack


def breadth_first_search(start, goal):
    queue = Queue(start)
    visited = []
    found = None

    while len(queue) > 0:
        node = queue.dequeue()

        if node.data is goal:
            found = node
            break

        if node not in visited:
            visited.append(node)

            for neighbor in node.neighbors:
                neighbor.previous = node
                queue.enqueue(neighbor)

    if found is not None:
        path = []
        while node.previous is not None:
            path.insert(0, node)
            node = node.previous
        path.insert(0, start)
        return path
    else:
        return None


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


def depth_first_search(start, goal):
    stack = Stack(start)
    visited = []
    found = None

    while len(stack) > 0:
        node = stack.pop()

        if node.data is goal:
            found = node
            break

        if node not in visited:
            visited.append(node.data)   # .data acts as a unique identifier

            for neighbor in node.neighbors:
                neighbor.previous = node
                stack.push(neighbor)

    if found is not None:
        path = []
        while node.previous is not None:
            path.insert(0, node)
            node = node.previous
        path.insert(0, start)
        return path
    else:
        return None


"""
Function aliases.
"""
bfs = breadth_first_search
dfs = depth_first_search
