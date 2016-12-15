#!/usr/bin/python
from random import randint


class RandomQueue:

    def __init__(self):
        self._items = []

    def insert(self, item):
        self._items.append(item)  # O(1)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        size = len(self._items)
        out = randint(0, size-1)
        self._items[out], self._items[-1] = self._items[-1], self._items[out]
        return self._items.pop()  # O(1)

    def is_empty(self):
        return not self._items

    def is_full(self):
        return False

rq = RandomQueue()
for i in range(10):
    rq.insert(i)
for i in range(10):
    print(rq.remove())
