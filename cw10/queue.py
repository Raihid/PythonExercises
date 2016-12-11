#!/usr/bin/python
import unittest


# Exercise 10.4
class Queue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        data = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue1 = Queue(5)
        self.queue2 = Queue(10)

    def test_is_empty(self):
        self.assertTrue(self.queue1.is_empty())
        self.queue1.put(5)
        self.assertFalse(self.queue1.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue1.is_full())
        for i in range(5):
            self.queue1.put(i)
        self.assertTrue(self.queue1.is_full())

    def test_put(self):
        try:
            for i in range(10):
                self.queue2.put(i)
        except ValueError as e:
            self.fail("Unexpected exception" + str(e))

        with self.assertRaises(ValueError):
            self.queue2.put(11)

    def test_get(self):
        self.queue1.put(1)
        self.queue1.put(2)
        self.assertEqual(self.queue1.get(), 1)
        self.assertEqual(self.queue1.get(), 2)

        with self.assertRaises(ValueError):
            self.queue2.get()

if __name__ == '__main__':
    unittest.main()
