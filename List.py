#!/usr/bin/env python3

from common import Node

class ListNode(Node.DoubleNode):
    __slots__ = ('previous', 'data', 'next')

    def __str__(self):
        return '{} <--> {}'.format(self.data, self.next)


class List:
    __slots__ = ('head', 'tail', 'size', 'node_type')

    def __init__(self, data=None, node_type=ListNode):
        self.node_type = node_type
        self.head = self.node_type(data)
        self.tail = self.head
        #self.current = self.tail

        if data is None:
            self.size = 0
        else:
            self.size = 1

    def __str__(self):
        if self.head.data is not None:
            return '{}'.format(self.head)
        else:
            return 'None'

    def __len__(self):
        return self.size

    def __contains__(self, data):
        if self.size == 0:
            return self.head.data is data

        node = self.head

        for i in range(self.size):
            if node.data == data:
                return True

            node = node.next

        return False

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError('list index out of range')

        node = self.head

        for i in range(index):
            node = node.next

        return node.data

    def __setitem__(self, index, data):
        if index >= self.size:
            return

        node = self.head

        for i in range(index+1):
            node = node.next

        node.data = data

    def __delitem__(self, index):
        return self.remove(index)

    # __iter__
    # __next__ ?

    def add(self, data):
        # Maybe combine with __setitem__
        if self.tail.data is None:
            self.tail.data = data
        else:
            node = self.node_type(data)
            node.previous = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def remove(self, index):
        if index >= self.size:
            return None
        elif index == 0:
            data = self.head.data
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = self.node_type(None)
            self.size -= 1
            return data
        elif index == len(self)-1:
            data = self.tail.data
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return data

        node = self.head

        for i in range(index):
            node = node.next

        data = node.data
        previous = node.previous
        previous.next = node.next
        node.next.previous = previous
        self.size -= 1
        return data

    #def clone(self):

    def reverse(self):
        head = self.head
        tail = self.tail
        node = self.tail

        while node is not None:
            n = node.next
            node.next = node.previous
            node.previous = n
            node = node.next

        self.tail = head
        self.head = tail


if __name__ == '__main__':
    l = [5, 2, 3, 1, 7, 9, 8]
    d = List()

    for e in l:
        d.add(e)

    print(len(d), '|', d)
    d.reverse()
    print(len(d), '|', d)

    d.remove(len(d)-1)
    print(len(d), '|', d, '*')

    for i in range(len(d)):
        d.remove(0)
        print(len(d), '|', d)
