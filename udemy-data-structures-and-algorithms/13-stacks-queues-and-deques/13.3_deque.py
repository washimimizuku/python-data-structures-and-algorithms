class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


d = Deque()
d.add_front('hello')
d.add_rear('world')
print(d.size())

print(d.remove_front() + ' ' + d.remove_rear())

print(d.size())
