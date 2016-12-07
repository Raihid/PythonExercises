#!/usr/bin/python
class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


# Exercise 9.7
def count_leafs(top):
    if top.left is None and top.right is None:
        return 1
    return (count_leafs(top.left) if top.left is not None else 0 +
            count_leafs(top.right) if top.right is not None else 0)


def count_total(top):
    return 1 + (count_total(top.left) if top.left is not None else 0 +
                count_total(top.right) if top.right is not None else 0)
