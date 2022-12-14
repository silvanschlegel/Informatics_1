class Tree(object):
    def __init__(self, val, left = None, right = None):
        assert type(val) == int
        assert left == None or type(left) == Tree
        assert right == None or type(right) == Tree
        self.val = val
        self.left = left
        self.right = right



def sumTree(tree):
    if tree == None:
        return 0
    counter = tree.val
    counter += sumTree(tree.left)
    counter += sumTree(tree.right)
    return counter

assert sumTree(None) == 0
assert sumTree(Tree(1)) == 1
assert sumTree(Tree(1, Tree(2))) == 3
assert sumTree(Tree(5, Tree(-1), Tree(-2))) == 2
assert sumTree(Tree(1, Tree(2, Tree(3, Tree(4))))) == 10





