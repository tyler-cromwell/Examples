#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/'+ os.pardir +'/')
from data_structures.node import GraphNode
from algorithms import graph


def construct_path(start, end):
    path = []
    node = end

    while node.previous is not None:
        path.insert(0, node)
        node = node.previous
    path.insert(0, start)

    return path


if __name__ == '__main__':
    print('====================')
    print('Breadth First Search')
    print('====================')

    node1 = GraphNode('Arad')
    node2 = GraphNode('Faragas')
    node3 = GraphNode('Zerind')
    node4 = GraphNode('Timisoara')
    node5 = GraphNode('Oradea')
    node6 = GraphNode('Lugoj')
    node7 = GraphNode('Sibiu')
    node8 = GraphNode('Rimnicu Vilcea')

    node1.edges = [(node3, 75), (node4, 118), (node7, 140)]
    node2.edges = [(node7, 99)]
    node3.edges = [(node1, 75), (node5, 71)]
    node4.edges = [(node1, 118), (node6, 111)]
    node5.edges = [(node3, 71), (node7, 151)]
    node6.edges = [(node4, 111)]
    node7.edges = [(node5, 151), (node1, 140), (node2, 99), (node8, 80)]
    node8.edges = [(node7, 80)]

    goals = [node6.id]
    solution = graph.breadth_first_search(node7, goals=goals)
    path = construct_path(node7, solution)
    print('Path: {},'.format(solution.total), ' -> '.join([str(node) for node in path]))
