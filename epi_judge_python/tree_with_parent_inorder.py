from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []

    node = tree
    while node.left:
        node = node.left

    res = []
    while node:
        res.append(node.data)
        node = getNextNode(node)
    return res

def getNextNode(node):
    if not node:
        return
    # if node has right child
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor
    else:
        if not node.parent:
            return
        child = node
        successor = child.parent
        while successor and successor.left != child:
            child = successor
            successor = successor.parent
        return successor
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
