from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if not tree:
        return False

    remaining_weight -= tree.data

    # leaf
    if not tree.left and not tree.right:
        return remaining_weight == 0

    # non-leaf
    if has_path_sum(tree.left, remaining_weight):
        return True
    if has_path_sum(tree.right, remaining_weight):
        return True

    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
