"""
implement the three basic traversals of binary trees:
inorder, preorder, and postorder.
"""


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal(root):  # Time: O(n) | Space: O(height)
    if root:
        # Preorder: Processes the root before the traversals
        # of left and right children.
        print('Preorder: %d' % root.data)

        tree_traversal(root.left)

        # Inorder: Processes the root after the traversal
        # of left child before the traversal of right child
        print('Inorder: %d' % root.data)

        tree_traversal(root.right)

        # Postorder: Processes the root after the traversals
        # of left and right children.
        print('Postorder: %d' % root.data)
