#!/usr/bin/python
class Node:
    """Klasa reprezentujaca wezel listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogolnie

    def str_all(self):
        rest = ", " + self.next.str_all() if self.next is not None else ""
        return str(self) + rest 

def remove_head(node):
    return [node.next, node.data] 

def remove_tail(node): # TODO: pustka
    if node.next == None:
        return [None, node.data]

    tail = node
    while tail.next.next:
        tail = tail.next
    data = tail.next.data 
    tail.next = None
    return [node, data]


def merge(node1, node2):
    if not node1:
        return node2

    old_tail = node1
    while old_tail: 
        old_tail = old_tail.next
    old_tail = node2
    return node1

def find_min(head):
    return find_best(head.next, head.data, lambda x, y: x > y)

def find_max(head):
    return find_best(head.next, head.data, lambda x, y: x < y)
    
def find_best(node, current_best, compare):
    if compare(current_best, node.data):
        current_best = node.data
    return (find_best(node.next, current_best, compare) if node.next
            else current_best)

head1 = None
head2 = None
head2 = Node(3, head2)
head2 = Node(2, head2)
print(merge(head1, head2).str_all())

# TODO: Uporzadkowac wszystko

# Zastosowanie.
# pusta lista

# head = Node("front")
# lista jednoelementowa

# Reczne budowanie dluzszej listy.
head = None                   # [], pusta lista
head = Node(3, head)          # [3]
head = Node(2, head)          # [2, 3]
head = Node(4, head)          # [4, 2, 3]

print(find_max(head))
print(find_min(head))
while head:
    head, data = remove_head(head)
    # head, data = remove_tail(head)
    print "usuwam", data
head = None
