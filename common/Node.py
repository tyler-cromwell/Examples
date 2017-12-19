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
