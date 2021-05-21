"""
Use a stack to print the entries of a
singly-linked list in reverse order.
"""


def print_linked_list_in_reverse(head):  # Time: O(n)
    nodes = []

    while head:
        nodes.append(head.data)
        head = head.next

    while nodes:
        print(nodes.pop())
