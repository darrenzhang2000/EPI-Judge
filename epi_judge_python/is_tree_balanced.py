from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math

class Res:
    def __init__(self, isValid=True, leftHeight=0, rightHeight=0):
        self.isValid = isValid
        self.leftSubTreeHeight = leftHeight
        self.rightSubTreeHeight = rightHeight
        self.maxHeight = max(leftHeight, rightHeight) + 1

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return postorder(tree).isValid


def postorder(node):
    if not node:
        return Res()
    leftRes = postorder(node.left) 
    rightRes = postorder(node.right)
    isValid = leftRes.isValid and rightRes.isValid and abs(leftRes.maxHeight - rightRes.maxHeight) <= 1
    return Res(isValid, leftRes.maxHeight, rightRes.maxHeight)
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
