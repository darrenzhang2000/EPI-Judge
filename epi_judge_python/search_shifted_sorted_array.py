from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    if not A:
        return
    if A[0] < A[-1]:
        return 0

    l, r = 0, len(A) - 1
    while l <= r:
        m = l + (r - l) // 2
        if l == r or A[m - 1] >= A[m] <= A[m + 1]:
            return m
        elif A[m] >= A[0]:
            l = m + 1
        elif A[m] < A[-1]:
            r = m - 1
        else:
            return 'something broke'
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
