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
class GraphEdge:
    def __init__(self, n1, n2, weight):
        self._node1 = n1
        self._node2 = n2
        self._weight = weight

class GraphNode:
    def __init__(self, label, neighbors=set()):
        self._label = label
        self._neighbors = neighbors

    def getLabel(self):
        return self._label

    def getNeighbors(self):
        return self._neighbors

    def getNeighborsLabels(self):
        return [neighbor.getLabel() for neighbor in self._neighbors]
"""


def depth_first_search_recursive(indent, graph, visited, node, ordering=None):
    visited.add(node)
    #print(indent, node, ' -> ', graph[node], sep='')
    for neighbor in graph[node]:
        if neighbor not in visited:
            #print(indent, 'Visiting ', neighbor, sep='')
            depth_first_search_recursive(indent+'    ', graph, visited, neighbor)
        #else:
        #    print(indent, 'Already visited ', neighbor, sep='')

    if ordering is not None:
        ordering.append(node)


def depth_first_search_iterative(indent, graph, visited, node, ordering=None):
    stack = [node]

    while stack:
        currentNode = stack.pop()
        if currentNode in visited:
            continue
        visited.add(currentNode)
        #print('Visiting ', currentNode, ' -> ', graph[currentNode], sep='')
        if ordering is not None:
            ordering.append(currentNode)

        for neighbor in list(graph[currentNode])[::-1]:
            if neighbor not in visited:
                #print(indent, 'Stacking ', neighbor, sep='')
                stack.append(neighbor)
            #else:
            #    print(indent, 'Already visited ', neighbor, sep='')


def breadth_first_search_iterative(indent, graph, visited, node):
    queue = [node]

    while queue:
        currentNode = queue.pop(0)
        if currentNode in visited:
            print('Skipping ', currentNode, sep='')
            continue
        visited.add(currentNode)
        #print('Visiting ', currentNode, ' -> ', graph[currentNode], sep='')

        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                #print(indent, 'Queueing ', neighbor, sep='')
                queue.append(neighbor)
            #else:
            #    print(indent, 'Already visited ', neighbor, sep='')


import heapq
"""
graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'A': 10, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 8, 'E': 2},
    'D': {'B': 2, 'C': 8, 'E': 5},
    'E': {'D': 5, 'C': 2}
}
"""


def dijkstras2(graph, start):
    shortest = {n: float('inf') for n in graph.keys()}
    edgeQueue = []
    heapq.heappush(edgeQueue, (0, start))

    while len(edgeQueue):
        totalCost, node = heapq.heappop(edgeQueue)
        if totalCost >= shortest[node]:
            continue

        shortest[node] = totalCost
        for neighbor, cost in graph[node].items():
            tentativeCost = totalCost+cost
            if tentativeCost < shortest[neighbor]:
                #print('Visiting', neighbor, tentativeCost, node)
                heapq.heappush(edgeQueue, (totalCost + cost, neighbor))

    return shortest

#print(dijkstras(graph, 'A'))


def prims(graph, start):
    heap = []
    mst = set()
    visited = {start}
    for neighbor, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, neighbor))

    #print(heap)
    while len(visited) < len(graph):
        weight, src, dst = heapq.heappop(heap)
        if dst in visited:
            continue
        visited.add(dst)
        mst.add((weight, src, dst))
        for neighbor, weight in graph[dst].items():
            if neighbor not in visited:
                heapq.heappush(heap, (weight, dst, neighbor))

    #print(visited)
    return mst
#print(prims(graph, 'A'))


"""
graphDirected = {
    'A': {'B': 10, 'C': 3},
    'B': {'D': 2},
    'C': {'E': 2},
    'D': {'F': 1},
    'E': {'F': 1},
    'F': {},
    'G': {'H': 1},
    'H': {}
}
"""


def topological_sort(graph):
    ordering = []
    visited = set()

    for node in graph:
        depth_first_search_recursive('', graph, visited, node, ordering=ordering)

    ordering.reverse()
    return ordering

#print(graphDirected)
#print(topological_sort(graphDirected))


"""
Function aliases.
"""
bfs = breadth_first_search
dfs = depth_first_search
dfs2 = depth_first_search_recursive
dfs3 = depth_first_search_iterative
bfs2 = breadth_first_search_iterative
