#!/usr/bin/python
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


# Exercise 9.9
def count_nodes(node):
    if node is None:
        raise ValueError
    count = 1
    start = node
    while start != node.next:
        count += 1
        node = node.next
    return count

N = 100
M = 20

head = Node(1)
head.next = head
node = head
for i in range(2, N+1):
    node.next = Node(i, head)
    node = node.next
print(count_nodes(node))
for i in range(M):
    node = node.next
    node.next = node.next.next
print(count_nodes(node))
