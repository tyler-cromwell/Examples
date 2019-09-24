class SingleNode:
    __slots__ = ('data', 'next')

    def __init__(self, data, nex=None):
        self.data = data
        self.next = nex

    def __str__(self):
        return '{}'.format(self.data)

    def setnext(self, node):
        self.next = node
        self.next.previous = self


class DoubleNode:
    __slots__ = ('previous', 'data', 'next')

    def __init__(self, data, prev=None, nex=None):
        self.previous = prev
        self.data = data
        self.next = nex

    def __str__(self):
        return '{}'.format(self.data)

    def setprevious(self, node):
        self.previous = node
        self.previous.next = self

    def setnext(self, node):
        self.next = node
        self.next.previous = self


class GraphNode:
    __slots__ = ('data', 'previous', 'cost', 'total', 'edges')

    def __init__(self, data, edges=[]):
        self.data = data
        self.previous = None    # Previous node along shortest path
        self.cost = 0           # Step cost to this node along shortest path
        self.total = 0          # Total cost to this node along shortest path
        self.edges = edges

    def __str__(self):
        return '{}'.format(self.data)


class BinaryNode:
    __slots__ = ('left', 'data', 'right')

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return '{}'.format(self.data)

    def children(self):
        if self.left is not None and self.right is not None:
            return [self.left, self.right]
        elif self.left is not None and self.right is None:
            return [self.left]
        elif self.left is None and self.right is not None:
            return [self.right]
        else:
            return []

    def setleft(self, node):
        self.left = node

    def setright(self, node):
        self.right = node
