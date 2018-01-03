#!/usr/bin/env python3

from common import Node
import List


class QueueNode(Node.DoubleNode):
    __slots__ = ('previous', 'data', 'next')

    def __str__(self):
        return '{} <- {}'.format(self.next, self.data)


class Queue:
    __slots__ = ('list')

    def __init__(self, data=None):
        self.list = List.List(data=data, node_type=QueueNode)

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)

    def __contains__(self, data):
        return data in self.list

    def __getitem__(self, index):
        return self.list[index]

    def __delitem__(self, index):
        return self.list.remove(index)

    def peek(self):
        return self.list[0]

    def enqueue(self, data):
        self.list.add(data)

    def dequeue(self):
        return self.list.remove(0)

    def clone(self):
        l = self.list.clone()
        queue = Queue()

        for i in range(len(l)):
            queue.enqueue(l[i])

        return queue


if __name__ == '__main__':
    q = Queue(4)
    print('Size:', len(q))
    print('Is 5 in q:', 5 in q)
    print('q[0] =', q[0])
    print('Front:', q.peek())
    print(q)
    q.enqueue(5)
    q.enqueue(1)
    print(q)
    print(q.clone())
    del q[0]
    q.dequeue()
    print(q)
