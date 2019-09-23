#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/'+ os.pardir +'/')
from data_structures.node import GraphNode
from algorithms import graph


if __name__ == '__main__':
    print('====================')
    print('Depth First Search')
    print('====================')

    node1 = GraphNode('Arad')
    node2 = GraphNode('Faragas')
    node3 = GraphNode('Zerind')
    node4 = GraphNode('Timisoara')
    node5 = GraphNode('Oradea')
    node6 = GraphNode('Lugoj')
    node7 = GraphNode('Sibiu')
    node8 = GraphNode('Mehadia')
    node9 = GraphNode('Rimnicu Vilcea')

    node5.neighbors = [(151, node7)]
    node6.neighbors = [(70, node8)]
    node3.neighbors = [(71, node5)]
    node7.neighbors = [(99, node2), (80, node9)]
    node4.neighbors = [(111, node6)]
    node1.neighbors = [(75, node3), (140, node7), (118, node4)]

    path = graph.depth_first_search(node1, node9.data)
    print([node.data for node in path])
