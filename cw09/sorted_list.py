class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class SortedList:
    def __init__(self, *arguments):
        self.length = 0
        self.head = None 
        self.tail = None
        for item in arguments:
            self.insert(item)

    def __str__(self):
        desc = "["
        current_node = self.head
        while current_node is not None:
            desc += str(current_node) + " "
            current_node = current_node.next
        desc += "]"
        return desc
        
    def is_empty(self): 
        return self.length == 0

    def count(self):
        return self.length

    def insert(self, data):
        self.length += 1
        if self.head is None:
            self.head = Node(data, None)
        elif self.head.data < data:
            self.head = Node(data, self.head)
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.data > data:
                current_node = current_node.next
            current_node.next = Node(data, current_node.next)


    def remove(self):
        if self.is_empty():
            raise ValueError
        self.length -= 1
        old_head = self.head
        self.head = self.head.next
        return old_head.data


sl = SortedList(1, 2, 5, 3, 10, 100)
print(sl)
while not sl.is_empty():
    print(str(sl.remove()) + " Pozostalo: " + str(sl.count())) 
