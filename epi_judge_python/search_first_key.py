from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    l, r = 0, len(A) - 1
    while l <= r:
        m = l + (r - l) // 2
        if A[m] == k:
            if m == 0 or A[m - 1] != A[m]:
                return m
            else:
                r = m - 1
        elif A[m] < k:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
