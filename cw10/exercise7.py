class PriorityQueue:
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
        return self.items.pop(maxi)
