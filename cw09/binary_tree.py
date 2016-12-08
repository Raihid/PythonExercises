#!/usr/bin/python
class Node:
    """Class representing a node in binary tree"""

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
    return ((count_leafs(top.left) if top.left is not None else 0) +
            (count_leafs(top.right) if top.right is not None else 0))


def calc_total(top):
    return top.data + ((calc_total(top.left) if top.left is not None else 0) +
                       (calc_total(top.right) if top.right is not None else 0))


top = Node(1)
top.left = Node(24)
top.right = Node(-18)
top.left.right = Node(107)
top.left.left = Node(53)
top.right.left = Node(5)


print(count_leafs(top))
print(calc_total(top))
