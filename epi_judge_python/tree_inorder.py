from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    res = []
    s = [tree]
    while s:
        n = s[-1]
        if n.left:
            s.append(n.left)
            n.left = None
        else:
            s.pop()
            res.append(n.data)
            if n.right:
                s.append(n.right) 

    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
