'''
Write a function that takes a head node and an integer value n and then
returns the nth to last node in the linked list.
'''

from nose.tools import assert_equal


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def nth_to_last_node(n, head):

    left = head
    right = head

    # Set right pointer at n nodes away from head
    for i in range(n - 1):

        # Check for edge case of not having enough nodes!
        if not right.next:
            raise LookupError("Error: n is larger than the linked list.")

        # Otherwise, we can set the block
        right = right.next

    # Move the block down the linked list
    while right.next:
        left = left.next
        right = right.next

    # Now returns left pointer, its at the nth to last element:
    return left


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


class TestNLast(object):

    def test(self, sol):

        assert_equal(sol(2, a), d)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestNLast()
t.test(nth_to_last_node)
