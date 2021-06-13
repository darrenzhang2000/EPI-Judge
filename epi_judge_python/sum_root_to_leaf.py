from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

class Result:
    def __init__(self):
        self.total = 0
    def add(self, nBin):
        self.total += int(nBin, 2)

def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    r = Result()
    preorder(tree, r, path=[])
    return r.total

def preorder(tree, r, path):
    if not tree:
        return
    path.append(str(tree.data))
    if not tree.left and not tree.right:
        r.add("".join(path))
    preorder(tree.left, r, path)
    preorder(tree.right, r, path)
    path.pop()

# def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
#     r = Result()
#     preorder(tree, r, path=[])
#     return r.total

# def preorder(tree, r, path):
#     if not tree:
#         return
#     newPath = path + [str(tree.data)]
#     if not tree.left and not tree.right:
#         r.add("".join(newPath))
#     preorder(tree.left, r, newPath)
#     preorder(tree.right, r, newPath)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
