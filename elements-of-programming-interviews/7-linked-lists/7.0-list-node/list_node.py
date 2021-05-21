"""
A singly linked list is a data structure that contains
a sequence of nodes such that each node contains an
object and a reference to the next node in the list.
"""


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


# Search for a key in a linked list.
def search_list(linked_list, key):
    while linked_list and linked_list.data != key:
        linked_list = linked_list.next

    return linked_list


# Insert a new node after a specified node.
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


# Delete the following node, assuming it is not the tail.
def delete_after(node):
    node.next = node.next.next
