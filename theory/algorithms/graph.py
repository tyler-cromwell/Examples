#!/usr/bin/env python3

import itertools
import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/')
from data_structures.Queue import Queue
from data_structures.Stack import Stack


def breadth_first_search(start, goals=[]):
    queue = Queue((
        start,
        start.previous,
        start.cost,
        start.total
    ))
    visited = {}
    result = None

    while len(queue) > 0:
        node, previous, single, total = queue.dequeue()
        key = node.id

        if key not in visited or total < visited[key]:
            node.previous = previous
            node.cost = single
            node.total = total
            visited[key] = total

            if key in goals:
                result = node

            for neighbor, cost in node.expand_neighbors():
                queue.enqueue((
                    neighbor,
                    node,
                    cost,
                    total + cost
                ))

    return result


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


def depth_first_search(start, goals=[]):
    stack = Stack((
        start,
        start.previous,
        start.cost,
        start.total
    ))
    visited = {}
    result = None

    while len(stack) > 0:
        node, previous, single, total = stack.pop()
        key = node.id

        if key not in visited or total < visited[key]:
            node.previous = previous
            node.cost = single
            node.total = total
            visited[key] = total

            if key in goals:
                result = node

            for neighbor, cost in node.expand_neighbors():
                stack.push((
                    neighbor,
                    node,
                    cost,
                    total + cost
                ))

    return result


"""
Function aliases.
"""
bfs = breadth_first_search
dfs = depth_first_search
