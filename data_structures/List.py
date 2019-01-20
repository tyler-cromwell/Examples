#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')

from _common import Node


class ListNode(Node.DoubleNode):
    __slots__ = ('previous', 'data', 'next')

    def __str__(self):
        return '{} <--> {}'.format(self.data, self.next)


class List:
    __slots__ = ('head', 'tail', 'size', 'iters', 'node_type')


    def __init__(self, data=None, node_type=ListNode):
        self.node_type = node_type
        self.iters = 0

        if data is None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = self.node_type(data)
            self.tail = self.head
            self.size = 1


    def __str__(self):
        if self.head is None:
            return 'None'
        else:
            return '{}'.format(self.head)


    def __len__(self):
        return self.size


    def __contains__(self, data):
        node = self.head

        for i in range(self.size):
            if node.data == data:
                return True

            node = node.next

        return False


    def __getitem__(self, index):
        if index >= self.size or index < 0:
            raise IndexError('list index out of range')

        node = self.head

        for i in range(index):
            node = node.next

        return node.data


    def __setitem__(self, index, data):
        if index >= self.size or index < 0:
            raise IndexError('list index out of range')

        node = self.head

        for i in range(index+1):
            node = node.next

        node.data = data


    def __delitem__(self, index):
        return self.remove(index)


    def __iter__(self):
        return self


    def __next__(self):
        if self.iters < self.size:
            i = self.iters
            self.iters += 1
            return self[i]
        else:
            self.iters = 0
            raise StopIteration


    def add(self, data):
        if self.head is None:
            self.head = self.node_type(data)
            self.tail = self.head
            self.size += 1
        else:
            self.insert(self.size-1, data)


    def insert(self, index, data):
        node = self.node_type(data)

        if self.size == 0:
            self.head = node
            self.tail = self.head
            self.size += 1
        elif index == self.size-1:
            node.previous = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            self.size += 1
        elif index == 0:
            node.next = self.head
            node.previous = None
            self.head.previous = node
            self.head = node
            self.size += 1
        elif 0 < index and index < self.size-1:
            current = self.head

            for i in range(index):
                current = current.next

            node.previous = current
            node.next = current.next
            current.next.previous = node
            current.next = node
            self.size += 1
        else:
            raise IndexError('list index out of range')


    def remove(self, index):
        if index >= self.size or index < 0:
            raise IndexError('list index out of range')
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


    def clone(self):
        newlist = List(node_type=self.node_type)

        for i in range(self.size):
            newlist.add(self[i])

        return newlist


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

    print(len(l), '|', l)

    for e in l:
        d.add(e)

    for n in d:
        print(n)

    print('-------------')
    print(len(d), '|', d)
    print(len(d), '|', d.clone(), 'c')
    d.reverse()
    print(len(d), '|', d)

    d.remove(len(d)-1)
    print(len(d), '|', d, '*')

    for i in range(len(d)):
        d.remove(0)
        print(len(d), '|', d)

    print('-------------')
    d = List(5)
    print(d)
    d.remove(0)
    print(d)
    d.add(2)
    d.add(3)
    print(d)
