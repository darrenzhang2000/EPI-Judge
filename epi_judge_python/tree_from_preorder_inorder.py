from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

class PreorderIdx:
    def __init__(self):
        self.idx = 0

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    if not preorder: 
        return 
    preorderIdx = PreorderIdx()
    valueIndexMap = {v: i for i, v in enumerate(inorder)}
    return r(preorder, inorder, preorderIdx, 0, len(preorder) - 1, valueIndexMap)

def r(preorder, inorder, preorderIdx, left, right, valueIndexMap):
    if left > right:
        return

    value = preorder[preorderIdx.idx]
    preorderIdx.idx += 1

    root = BinaryTreeNode(value)
    rootIdx = valueIndexMap[value]
    root.left = r(preorder, inorder, preorderIdx, left, rootIdx - 1, valueIndexMap)
    root.right = r(preorder, inorder, preorderIdx, rootIdx + 1, right, valueIndexMap)
    return root


#     if not inorder:
#         return 
#     head = BinaryTreeNode(preorder[0])
#     inIdx = 0
#     appendLeft = True
#     nodeToAppendTo = head
#     ht = {preorder[0]: head}
#     for i in range(1, len(preorder)):
#         n = preorder[i]
#         print(n)
#         if n == inorder[inIdx]:
#             nodeToAppendTo = insert(nodeToAppendTo, BinaryTreeNode(n), appendLeft)
#             ht[n] = nodeToAppendTo
#             while inIdx + 1 < len(inorder) and  inorder[inIdx + 1] in ht:
#                 inIdx += 1
#             nodeToAppendTo = ht[inorder[inIdx]]
#             appendLeft = False
#         else:
#             nodeToAppendTo = insert(nodeToAppendTo, BinaryTreeNode(n), appendLeft)
#             ht[n] = nodeToAppendTo
#             appendLeft = True
#     print('return', head)
#     return head

# def findNode(head, n):
#     if head and head.data == n:
#         return head
#     if not head:
#         return None
#     return findNode(head.left, n) or findNode(head.right, n)


# def insert(pre, cur, appendLeft):
#     if appendLeft:
#         pre.left = cur
#     else:
#         pre.right = cur
#     return cur

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
