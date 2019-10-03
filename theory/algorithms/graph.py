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


def depth_first_search(start):
    stack = Stack((
        start,
        start.previous,
        start.cost,
        start.total
    ))
    visited = {}

    while len(stack) > 0:
        node, previous, single, total = stack.pop()

        if node not in visited:
            visited[node] = total

            for neighbor, cost in node.edges:
                neighbor.previous = node
                neighbor.cost = cost
                neighbor.total = total + neighbor.cost
                stack.push((
                    neighbor,
                    neighbor.previous,
                    neighbor.cost,
                    neighbor.total
                ))
        elif total < visited[node]:
            node.previous = previous
            node.cost = single
            node.total = total + node.cost
            visited[node] = total

    return visited


"""
Function aliases.
"""
bfs = breadth_first_search
dfs = depth_first_search
