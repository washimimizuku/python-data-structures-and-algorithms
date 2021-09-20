'''
https://www.hackerrank.com/challenges/30-binary-search-trees

The height of a binary search tree is the number of edges between the
tree's root and its furthest leaf. You are given a pointer, root, pointing
to the root of a binary search tree. Complete the getHeight function
provided in your editor so that it returns the height of the binary search tree.
'''


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        num_left = 0
        num_right = 0
        if root.left:
            num_left = 1 + self.getHeight(root.left)
        if root.right:
            num_right = 1 + self.getHeight(root.right)

        if num_left > num_right:
            return num_left
        else:
            return num_right


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
