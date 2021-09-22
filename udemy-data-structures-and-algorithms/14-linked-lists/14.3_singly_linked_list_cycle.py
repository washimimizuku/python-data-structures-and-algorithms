'''
Given a singly linked list, write a function which takes in the
first node in a singly linked list and returns a boolean indicating
if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous
node in the list. This is also sometimes known as a circularly linked list.
'''

from nose.tools import assert_equal


class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None


def cycle_check(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.next != None:

        # Note
        marker1 = marker1.next
        marker2 = marker2.next.next

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a  # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z


#############
class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")


# Run Tests
t = TestCycleCheck()
t.test(cycle_check)
