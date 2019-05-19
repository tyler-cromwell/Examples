#!/usr/bin/env python3

import enum
import itertools
import sys

sys.path.append('../../')
from data_structures import Queue


class Traversal(enum.Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


def breadth_first_search(root):
    queue = Queue.Queue(root)
    visited = []

    while len(queue) > 0:
        node = queue.dequeue()

        if node not in visited:
            visited.append(node.data)

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


# TODO: FIX!
def depth_first_search(root, traversal=Traversal.INORDER):
    visited = []

    if traversal == Traversal.PREORDER:
        visited.append(root.data)

        if root.left is not None:
            visited += depth_first_search(root.left, traversal)
 
        if root.right is not None:
            visited += depth_first_search(root.right, traversal)

    elif traversal == Traversal.POSTORDER:
        if root.left is not None:
            visited += depth_first_search(root.left, traversal)
 
        if root.right is not None:
            visited += depth_first_search(root.right, traversal)

        visited.append(root.data)

    else:
        if root.left is not None:
            visited += depth_first_search(root.left, traversal)

        visited.append(root.data)

        if root.right is not None:
            visited += depth_first_search(root.right, traversal)

    return visited
