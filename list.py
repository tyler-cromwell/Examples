#!/usr/bin/env python3

from common import Node

class ListNode(Node.DoubleNode):
    __slots__ = ('previous', 'data', 'next')

    def __str__(self):
        return '{} -> {}'.format(self.data, self.next)


class List:
    __slots__ = ('head', 'tail', 'size')

    def __init__(self, data=None):
        self.head = ListNode(data)
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

    #def __contains__(self, data):

    def __getitem__(self, index):
        if index >= self.size:
            return None

        node = self.head

        for i in range(index+1):
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
        pass

    # __iter__
    # __next__ ?

    def add(self, data):
        # Maybe combine with __setitem__
        if self.tail.data is None:
            self.tail.data = data
        else:
            node = ListNode(data)
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
                self.head = ListNode(None)
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

    for e in l:
        d.remove(0)

    print(len(d), '|', d)
