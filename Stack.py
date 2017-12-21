#!/usr/bin/env python3

from common import Node
import List


class StackNode(Node.DoubleNode):
    __slots__ = ('previous', 'data', 'next')

    def __str__(self):
        return '{} -> {}'.format(self.data, self.next)


class Stack:
    __slots__ = ('list')

    def __init__(self, data=None):
        self.list = List.List(data=data, node_type=StackNode)

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)

    def peek(self):
        return self.list[len(self)-1]

    def push(self, data):
        self.list.add(data)

    def pop(self):
        return self.list.remove(len(self)-1)


if __name__ == '__main__':
    l = [5, 2, 3, 1, 7, 9]
    s = Stack()

    for e in l:
        s.push(e)
        print('Size:', len(s), '| Top:', s.peek(), '| Stack:', s)

    for e in range(len(s)):
        print('Size:', len(s), '| Removed:', s.pop(), '| Stack:', s)
