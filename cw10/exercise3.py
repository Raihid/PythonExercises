#!/usr/bin/python
class Stack:

    def __init__(self, size=100):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size
        self.numbers = size * [False]

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if not isinstance(data, int) or data > size-1:
            return  
        self.items[self.n] = data
        self.n = self.n + 1

    def pop(self):
        self.n = self.n - 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data
