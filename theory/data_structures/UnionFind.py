#!/usr/bin/env python3

class UnionFind:
    def __init__(self, graph={}):
        self._parent = {}
        self._rank = {}

        for node in graph:
            self._parent[node] = node
            self._rank[node] = 0

    def find(self, node):
        if node not in self._parent:
            self._parent[node] = node
            self._rank[node] = 0
        if node != self._parent[node]:
            self._parent[node] = self.find(self._parent[node])
        return self._parent[node]

    def union(self, node1, node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            # Cycle detected
            return False

        rank1 = self._rank[rep1]
        rank2 = self._rank[rep2]

        if rank1 > rank2:
            self._parent[rep2] = rep1
        elif rank2 > rank1:
            self._parent[rep1] = rep2
        else:
            self._parent[rep1] = rep2
            self._rank[rep2] += 1

        return True
