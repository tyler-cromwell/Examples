#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.getcwd() +'/'+ sys.argv[0]) +'/'+ os.pardir +'/'+ os.pardir +'/')
from data_structures.node import GraphNode
from algorithms import graph


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
    node8 = GraphNode('Mehadia')
    node9 = GraphNode('Rimnicu Vilcea')

    node5.neighbors = [node7]
    node6.neighbors = [node8]
    node3.neighbors = [node5]
    node7.neighbors = [node2, node9]
    node4.neighbors = [node6]
    node1.neighbors = [node3, node7, node4]

    path = graph.depth_first_search(node1, 'Rimnicu Vilcea')
    print([node.data for node in path])
