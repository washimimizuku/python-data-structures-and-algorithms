'''
Given a binary tree of integers, print it in level order.
The output will contain space between the numbers in the same
level, and new line between different levels.

For example, if the tree is:

    1
   / \
  2   3
 /   / \
4   5   6

The output should be:

1 
2 3 
4 5 6
'''


import collections


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def levelOrderPrint(tree):

    if not tree:
        return

    nodes = collections.deque([tree])
    current_count, next_count = 1, 0

    while len(nodes) != 0:
        current_node = nodes.popleft()
        current_count -= 1
        print(current_node.val, end=' ')

        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1

        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1

        if current_count == 0:
            # finished printing current level
            print('\n')
            current_count, next_count = next_count, current_count


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6)

levelOrderPrint(root)
