import bintrees


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


# BST search
def search_bst(tree, key):
    return (tree
            if not tree or tree.data == key else search_bst(tree.left, key)
            if key < tree.data else search_bst(tree.right, key))


t = bintrees.RBTree([(5, 'Alfa '), (2, 'Bravo'),
                    (7, 'Charlie'), (3, 'Delta '), (6, 'Echo')])

print(t[2])  # 'Bravo'
print(t.min_item(), t.max_item())  # (2, 'Bravo'), (7, 'Charlie')

# {2: 'Bravo', 3: 'Delta', 5: 'Alfa', 6 'Echo', 7: 'Charlie', 9: 'Golf']
t.insert(9, 'Golf')
print(t)

print(t.min_key(), t.max_key())  # 2, 9

t.discard(3)
print(t)  # {2: 'Bravo', 5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'}

# a = (2: 'Bravo')
a = t.pop_min()
print(a)
print(t)  # {5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'}

# b = (9: 'Golf')
b = t.pop_max()
print(b)
print(t)  # {5: 'Alfa', 6: 'Echo', 7: 'Charlie'}
