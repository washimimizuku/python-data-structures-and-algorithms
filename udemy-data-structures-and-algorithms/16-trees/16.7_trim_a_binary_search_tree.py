'''
Given the root of a binary search tree and 2 numbers min and max,
trim the tree such that all the numbers in the new tree are between
min and max (inclusive). The resulting tree should still be a valid
binary search tree. So, if we get this tree as input:

    8
   /  \
  3    10
 / \     \
1   6     14 
   / \    / 
  4   7  13

and we’re given min value as 5 and max value as 13, then the
resulting binary search tree should be:

 8
/ \
6  10
 \  \
  7  13

We should remove all the nodes whose value is not between min and max.
'''


import collections


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def level_order_print(tree):

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


def trim_bst(tree, min_val, max_val):

    if not tree:
        return

    tree.left = trim_bst(tree.left, min_val, max_val)
    tree.right = trim_bst(tree.right, min_val, max_val)

    if min_val <= tree.val <= max_val:
        return tree

    if tree.val < min_val:
        return tree.right

    if tree.val > max_val:
        return tree.left


root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)


level_order_print(root)

trim_bst(root, 5, 13)

level_order_print(root)
