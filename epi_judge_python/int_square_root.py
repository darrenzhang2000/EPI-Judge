from test_framework import generic_test


def square_root(k: int) -> int:
    l, r = 0, k
    while l <= r:
        m = l + (r - l) // 2
        if m*m == k or m*m < k and (m+1)*(m+1) > k:
            return m
        elif m*m<k:
            l = m + 1
        else:
            r = m - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
