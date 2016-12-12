#!/usr/bin/python
from random import randint


class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)  # O(1)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        size = len(self.items)
        out = randint(0, size-1)
        self.items[out], self.items[-1] = self.items[-1], self.items[out]
        return self.items.pop()  # O(1)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

rq = RandomQueue()
for i in range(10):
    rq.insert(i)
for i in range(10):
    print(rq.remove())
