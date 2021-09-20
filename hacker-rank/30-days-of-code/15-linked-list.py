'''
https://www.hackerrank.com/challenges/30-linked-list

Complete the insert function in your editor so that it creates a new Node
(pass data as the Node constructor argument) and inserts it at the tail of
the linked list referenced by the head parameter. Once the new node is added,
return the reference to the head node.

Note: The head argument is null for an empty list.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head == None:
            head = Node(data)
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = Node(data)
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
