from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def checkSym(n1, n2):
        if n1 == None and n2 == None:
            return True
        elif n1 and n2 and n1.data == n2.data:
            left0, left1 = n1.left, n1.right 
            right0, right1 = n2.left, n2.right
            return checkSym(left0, right1) and checkSym(left1, right0)
        return False

    return not tree or checkSym(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
