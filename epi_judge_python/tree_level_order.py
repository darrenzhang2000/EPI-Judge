from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    res = []
    q = deque([tree])
    while q:
        curLevelRes = []
        nextQ = deque()
        while q:
            node = q.popleft()
            curLevelRes.append(node.data)
            if node.left: 
                nextQ.append(node.left)
            if node.right:
                nextQ.append(node.right)
        res.append(curLevelRes)
        q = nextQ
    return res

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
