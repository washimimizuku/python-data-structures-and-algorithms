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

    def breadth_first_search_iterative(self):
        current_node = self.root
        my_list = []
        queue = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            my_list.append(current_node.data)
            if (current_node.left):
                queue.append(current_node.left)
            if (current_node.right):
                queue.append(current_node.right)

        return my_list
            

    def breadth_first_search_recursive(self, queue, my_list):
        if len(queue) == 0:
            return my_list

        current_node = queue.pop(0)
        my_list.append(current_node.data)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

        return self.breadth_first_search_recursive(queue, my_list)


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(6)
binary_search_tree.insert(20)
binary_search_tree.insert(170)
binary_search_tree.insert(15)
binary_search_tree.insert(1)

print(binary_search_tree.breadth_first_search_iterative())
print(binary_search_tree.breadth_first_search_recursive([binary_search_tree.root], []))