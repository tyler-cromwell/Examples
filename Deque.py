#!/usr/bin/env python3

from common import Node
import List
import Queue


class DequeNode(Node.DoubleNode):
    __slots__ = ('previous', 'data', 'next')

    def __str__(self):
        return '{} <--> {}'.format(self.next, self.data)


class Deque(Queue.Queue):
    def __init__(self, data=None):
        self.list = List.List(data=data, node_type=DequeNode)

    def __str__(self):
        return str(self.list) + ' <--> None'

    def enqueuefront(self, data):
        self.list.reverse()
        self.list.add(data)
        self.list.reverse()

    def dequeueback(self):
        return self.list.remove(len(self)-1)


if __name__ == '__main__':
    d = Deque(7)
    print('Size:', len(d))
    print(d)
    d.enqueue(2)
    d.enqueue(5)
    d.enqueuefront(3)
    print('Size:', len(d))
    print(d)
