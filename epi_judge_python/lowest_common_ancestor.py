import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import namedtuple

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        Status = namedtuple("Status", ("numTargetNodes" ,"ancestor"))
        def helper(tree, node0, node1):
            if not tree:
                return Status(0, None)

            leftStatus = helper(tree.left, node0, node1)
            if leftStatus.numTargetNodes == 2:
                return leftStatus

            rightStatus = helper(tree.right, node0, node1)
            if rightStatus.numTargetNodes == 2:
                return rightStatus
            
            numTargetNodes = leftStatus.numTargetNodes + rightStatus.numTargetNodes + [node0, node1].count(tree)

            return Status(numTargetNodes, tree if numTargetNodes == 2 else None)
        return helper(tree, node0, node1).ancestor



# def findPath(tree, node, res, path):
#     if not tree:
#         return
#     path.append(tree)
#     if tree is node:
#         res.path = path[:]
#     findPath(tree.left, node, res, path)
#     findPath(tree.right, node, res, path)
#     path.pop()

# class Result:
#     def __init__(self):
#         self._found = False
#         self.path = []

# def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
#         node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
#         leftR = Result()
#         findPath(tree, node0, leftR, [])
#         rightR = Result()
#         findPath(tree, node1, rightR, [])
#         path0 = leftR.path
#         path1 = rightR.path
#         for i in range(min(len(path0), len(path1)) - 1, -1, -1):
#             if path0[i] is path1[i]:
#                 return path0[i]

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
