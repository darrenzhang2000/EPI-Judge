from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    '''
    1 1 1 1 1 5 10 25
    keep looping and incrementing by 1:
    1 -> 1
    2 -> 1 + 1
    3 -> 1 + 1 + 1
    4 -> 1 + 1 + 1 + 1
    5 -> either 5 in ht or add 1 to 4
    9 -> 8 + 1
    10 -> in ht
    15 -> 14 + 1 

    sort A
    for each number n, see if n can be constructed using smaller coins. 
    -> n^2
    '''
    A.sort()
    v = 0
    for n in A:
        if n > v + 1:
            break
        v += n
    return v + 1

    # A.sort()
    # if not A or A[0] != 1:
    #     return 1
    # v = 1
    # for i in range(1, len(A)):
    #     n = A[i]
    #     if n <= v or n == v + 1:
    #         v += n
    #     else:
    #         break
    # return v + 1

# [1, 2, 3, 7]
#           ^
# v=13



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
