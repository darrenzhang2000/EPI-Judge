from typing import List

from test_framework import generic_test
from heapq import heappush, heappop, heapify

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    res = []
    arr_iters = [iter(sorted_arrays[i]) for i in range(len(sorted_arrays))]
    h = []
    for i in range(len(sorted_arrays)):
        firstEl = next(arr_iters[i], None)
        if firstEl != None:
            h.append((firstEl, i))
    heapify(h)
    while h:
        el, arr_it_idx = heappop(h)
        res.append(el)
        nextEl = next(arr_iters[arr_it_idx], None)
        if nextEl != None:
            heappush(h, (nextEl, arr_it_idx))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
