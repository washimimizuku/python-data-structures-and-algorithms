class Node(object):

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)

# Setting b after a
b.prev = a
a.next = b

# Setting c after a
c.prev = b
b.next = c

print(b.value)
print(b.prev.value)
print(b.next.value)
