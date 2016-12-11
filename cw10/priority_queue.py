#!/usr/bin/python


# Exercise 10.5, Exercise 10.7
class PriorityQueuePythonic:
    def __init__(self, cmpfunc=cmp):
        self.items = []
        self.cmpfunc = cmpfunc

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if cmpfunc(self.items[i], self.items[maxi]) == 1:
                maxi = i
        self.items[maxi], self.items[-1] = self.items[-1], self.items[maxi]
        return self.items.pop()


class PriorityQueueAsArray:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def insert(self, data):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.items[self.n] = data
        self.n = self.n + 1

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        maxi = 0
        for i in range(self.n):
            if self.items[i] > self.items[maxi]:
                maxi = i
        self.n = self.n - 1
        data = self.items[maxi]
        self.items[maxi] = self.items[self.n]
        self.items[self.n] = None
        return data


# TODO: Testy 
