#!/usr/bin/python
import unittest


def cmp(x, y):  # Fix for Python3
    if x == y:
        return 0
    if x > y:
        return 1
    else:
        return -1


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
        if self.is_empty():
            raise ValueError("Queue is empty!")
        maxi = 0
        for i in range(1, len(self.items)):
            if self.cmpfunc(self.items[i], self.items[maxi]) == 1:
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


class PriorityQueueTest(unittest.TestCase):

    def setUp(self):
        self.pq1 = PriorityQueuePythonic()
        self.pq2 = PriorityQueueAsArray(10)
        self.pq3 = PriorityQueuePythonic(cmpfunc=lambda x, y:
                                         cmp(abs(x), abs(y)))

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            self.pq1.remove()
        with self.assertRaises(ValueError):
            self.pq2.remove()
        for i in range(10):
            self.pq2.insert(i)
        with self.assertRaises(ValueError):
            self.pq2.insert(5)

    def test_cmp(self):
        for i in range(-11, 0, 2):
            self.pq3.insert(i)
        for i in range(0, 11, 2):
            self.pq3.insert(i)
        self.assertEqual(self.pq3.remove(), -11)
        self.assertEqual(self.pq3.remove(), 10)
        self.assertEqual(self.pq3.remove(), -9)
        self.assertEqual(self.pq3.remove(), 8)
        self.assertEqual(self.pq3.remove(), -7)

if __name__ == '__main__':
    unittest.main()
