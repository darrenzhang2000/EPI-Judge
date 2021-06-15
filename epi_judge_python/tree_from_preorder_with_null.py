import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class State:
    def __init__(self):
        self.state = 0

def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    return r(iter(preorder))

def r(preorderIt):
    value = next(preorderIt)

    if not value:
        return

    node = BinaryTreeNode(value)
    node.left = r(preorderIt)
    node.right = r(preorderIt)
    return node

# def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # if not len(preorder):
    #     return 0
    # parentHt = {}
    # head = nodeToAppendTo = BinaryTreeNode(preorder[0])
    # s = State()
    # for n in preorder:
    #     if n == None:
    #         s.state += 1
    #         if s.state == 2:
    #             # get parent with only 1 child
    #             nodeToAppendTo = parentHt[nodeToAppendTo.data]
    #             while nodeToAppendTo and parentHt[nodeToAppendTo.data].right != None:
    #                 nodeToAppendTo = parentHt[nodeToAppendTo.data]
    #             s.state = 0
    #     elif s.state == 0:
    #         nodeToAppendTo.left = BinaryTreeNode(n)
    #         parentHt[n] = nodeToAppendTo
    #         nodeToAppendTo = nodeToAppendTo.left
    #     elif s.state == 1:
    #         nodeToAppendTo.right = BinaryTreeNode(n)
    #         parentHt[n] = nodeToAppendTo
    #         nodeToAppendTo = nodeToAppendTo.right
    #         s.state = 0
    # print(head)
    # return head


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
