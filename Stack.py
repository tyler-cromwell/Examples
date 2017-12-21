#!/usr/bin/env python3

from common import Node


class StackNode(Node.DoubleNode):
    __slots__ = ('previous', 'data', 'next')

    def __str__(self):
        return '{} -> {}'.format(self.data, self.next)


class Stack:
    __slots__ = ('base', 'tail', 'size')

    def __init__(self, data=None):
        self.base = StackNode(data)
        self.tail = self.base

        if data is None:
            self.size = 0
        else:
            self.size = 1

    def __str__(self):
        if self.base.data is not None:
            return '{}'.format(self.base)
        else:
            return 'None'

    def __len__(self):
        return self.size

    def peek(self):
        return self.tail.data

    def push(self, data):
        if self.base.data is None:
            self.base.data = data
        else:
            node = StackNode(data)
            node.previous = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def pop(self):
        if self.tail.previous is not None and self.tail.data is not None:
            data = self.tail.data
            self.tail.previous.next = self.tail.next
            self.tail = self.tail.previous
            self.size -= 1
            return data
        elif self.tail.previous is None and self.tail.data is not None:
            data = self.tail.data
            self.tail.data = None
            self.size -= 1
            return data
        else:
            return None


if __name__ == '__main__':
    l = [5, 2, 3, 1, 7, 9]
    s = Stack()

    for e in l:
        s.push(e)
        print('Size:', len(s), '| Top:', s.peek(), '| Stack:', s)

    for e in l:
        print('Size:', len(s), '| Removed:', s.pop(), '| Stack:', s)
