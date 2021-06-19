from typing import List

from test_framework import generic_test, test_utils
from heapq import heappush, heappop, heapify

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return
    
    candidates_max_heap = []
    candidates_max_heap.append((-A[0], 0))
    res = []
    for _ in range(k):
        idx = heappop(candidates_max_heap)[1]
        res.append(A[idx])
        # push children
        if 2 * idx + 1 < len(A):
            heappush(candidates_max_heap, (-A[2 * idx + 1], 2 * idx + 1 ))
        if 2 * idx + 2 < len(A):
            heappush(candidates_max_heap, (-A[2 * idx + 2], 2 * idx + 2))
    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
