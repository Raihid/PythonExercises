#!/usr/bin/python
from random import randint


class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        size = len(self.items)
        out = randint(0, size)
        self.items[out], self.items[-1] = self.items[-1], self.items[out]
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False
