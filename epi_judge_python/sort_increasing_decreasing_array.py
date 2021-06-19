from typing import List

from test_framework import generic_test
from sorted_arrays_merge import merge_sorted_arrays

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    critical_idxs = get_critical_idxs(A)
    sorted_arrs = get_sorted_arrs(critical_idxs, A)
    return merge_sorted_arrays(sorted_arrs)

def get_sorted_arrs(critical_idxs, A):
    res = []
    flip = False
    for i in range(len(critical_idxs) - 1):
        if not flip:
            if i == len(critical_idxs) - 1:
                res.append(A[critical_idxs:])
            else:
                res.append(A[critical_idxs[i]: critical_idxs[i + 1] + 1])
        else:
            if i == len(critical_idxs) - 1:
                res.append(list(reversed(A[critical_idxs[i] + 1:])))
            else:
                res.append(list(reversed(A[critical_idxs[i] + 1: critical_idxs[i + 1]])))
        flip = not flip
    return res
# [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1]
#  0  1  2  3  4  5  6  7   8  9  10 11 12
# 0 2 4 7 12
# 0-2
# 4-3



def get_critical_idxs(A):
    if not A:
        return
    res = [0]
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] > A[i + 1] or A[i - 1] > A[i] < A[i + 1]:
            res.append(i)
    res.append(len(A) - 1)
    return res
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
