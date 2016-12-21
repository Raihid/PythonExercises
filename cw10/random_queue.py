#!/usr/bin/python
from random import randint


class RandomQueue:

    def __init__(self, size=10):
        self._items = [0] * size
        self._n = 0

    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full")
        self._items[self._n] = item  # O(1)
        self._n += 1

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        out = randint(0, self._n - 1)
        self._n -= 1
        self._items[out], self._items[self._n] = (self._items[self._n],
                                                  self._items[out])
        return self._items[self._n]  # O(1)

    def is_empty(self):
        return self._n == 0

    def is_full(self):
        return len(self._items) == self._n

rq = RandomQueue()
for i in range(10):
    rq.insert(i)
assert(rq.is_full())
out_list = []
for i in range(10):
    out_list += [rq.remove()]
print(out_list)

assert(rq.is_empty())
