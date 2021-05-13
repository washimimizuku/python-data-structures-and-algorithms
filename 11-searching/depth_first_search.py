class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                elif data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
                    

    def lookup(self, data):
        current_node = self.root
        while True:
            if current_node == None:
                return False

            if current_node.data == data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def dfs_in_order(self, current_node, my_list):
        if current_node.left:
            self.dfs_in_order(current_node.left, my_list)
        my_list.append(current_node.data)
        if current_node.right:
            self.dfs_in_order(current_node.right, my_list)
        return my_list

    def dfs_pre_order(self, current_node, my_list):
        my_list.append(current_node.data)
        if current_node.left:
            self.dfs_pre_order(current_node.left, my_list)
        if current_node.right:
            self.dfs_pre_order(current_node.right, my_list)
        return my_list

    def dfs_post_order(self, current_node, my_list):
        if current_node.left:
            self.dfs_post_order(current_node.left, my_list)
        if current_node.right:
            self.dfs_post_order(current_node.right, my_list)
        my_list.append(current_node.data)
        return my_list


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(6)
binary_search_tree.insert(20)
binary_search_tree.insert(170)
binary_search_tree.insert(15)
binary_search_tree.insert(1)

print(binary_search_tree.dfs_in_order(binary_search_tree.root, []))
print(binary_search_tree.dfs_pre_order(binary_search_tree.root, []))
print(binary_search_tree.dfs_post_order(binary_search_tree.root, []))