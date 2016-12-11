#!/usr/bin/python
import unittest


# Exercise 10.2 and 10.3
class StackAsArray:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size
        self.present = size * [False]

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if (not isinstance(data, int) or data > self.size - 1 or
           self.present[data] is True):
            raise ValueError("Invalid argument!")
        if self.is_full():
            raise ValueError("Stack is full!")
        self.present[data] = True
        self.items[self.n] = data
        self.n = self.n + 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty!")
        self.n = self.n - 1
        data = self.items[self.n]
        self.present[data] = False
        self.items[self.n] = None
        return data


class TestStackAsArray(unittest.TestCase):

    def setUp(self):
        self.stack1 = StackAsArray()
        self.stack2 = StackAsArray(15)
        self.stack3 = StackAsArray(20)

    def test_is_empty(self):
        self.assertTrue(self.stack1.is_empty())
        self.stack1.push(5)
        self.assertFalse(self.stack1.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack2.is_full())
        for i in range(15):
            self.stack2.push(i)
        self.assertTrue(self.stack2.is_full())

    def test_push(self):
        try:
            for i in range(10):
                self.stack1.push(i)
        except ValueError as e:
            self.fail("Unexpected exception " + str(e))
        with self.assertRaises(ValueError):
            self.stack1.push(16)
        with self.assertRaises(ValueError):
            self.stack2.push(30)
        self.stack2.push(5)
        with self.assertRaises(ValueError):
            self.stack2.push(5)

    def test_pop(self):
        with self.assertRaises(ValueError):
            self.stack1.pop()

        for i in reversed(range(10)):
            self.stack1.push(i)
        self.assertEqual(self.stack1.pop(), 0)
        self.assertEqual(self.stack1.pop(), 1)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
