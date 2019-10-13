#!/usr/bin/env python3

import heapq
import itertools
import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/')
from data_structures.Queue import Queue
from data_structures.Stack import Stack


def breadth_first_search(start, goals=[]):
    queue = Queue((start, start.previous))
    visited = {start.id: True}

    while len(queue) > 0:
        node, previous = queue.dequeue()

        if node.id in goals:
            return node

        for neighbor, cost in node.expand_neighbors():
            if neighbor.id not in visited:
                visited[neighbor.id] = True
                neighbor.previous = node
                queue.enqueue((neighbor, node))

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


def depth_first_search(start, goals=[]):
    stack = Stack((start, start.previous))
    visited = {start.id: True}

    while len(stack) > 0:
        node, previous = stack.pop()

        if node.id in goals:
            return node

        for neighbor, cost in node.expand_neighbors():
            if neighbor.id not in visited:
                visited[neighbor.id] = True
                neighbor.previous = node
                stack.push((neighbor, node))

    return None


def dijkstras(start):
    pqueue = [(
        start,
        start.previous,
        start.cost,
        start.total
    )]
    heapq.heapify(pqueue)
    visited = {}

    while len(pqueue) > 0:
        node, previous, single, total = heapq.heappop(pqueue)
        key = node.id

        if key not in visited or total < visited[key]:
            node.previous = previous
            node.cost = single
            node.total = total
            visited[key] = total

            for neighbor, cost in node.expand_neighbors():
                heapq.heappush(pqueue, (
                    neighbor,
                    node,
                    cost,
                    total + cost
                ))

    return visited


"""
Function aliases.
"""
bfs = breadth_first_search
dfs = depth_first_search
