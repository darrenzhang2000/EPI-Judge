import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def findPath(tree, node, res, path):
    if not tree:
        return
    newPath = path[:] + [tree]
    if tree is node:
        res.path = newPath[:]
    findPath(tree.left, node, res, newPath)
    findPath(tree.right, node, res, newPath)

class Result:
    def __init__(self):
        self._found = False
        self.path = []

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        leftR = Result()
        findPath(tree, node0, leftR, [])
        rightR = Result()
        findPath(tree, node1, rightR, [])
        path0 = leftR.path
        path1 = rightR.path
        for i in range(min(len(path0), len(path1)) - 1, -1, -1):
            if path0[i] is path1[i]:
                return path0[i]

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
