from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    '''
    [2]
    [6,6]
    [14,11,12]
    [15,13,17,14]
    [14,18,15,17,18]
    '''
    if not triangle:
        return 0
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            prev_left = triangle[i - 1][j - 1] if j - 1 >= 0 else float('inf')
            prev_mid = triangle[i - 1][j] if 0 <= j < len(triangle[i - 1]) else float('inf')
            min_prev = min(prev_left, prev_mid)
            triangle[i][j] += min_prev
    return min(triangle[-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
