from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    '''
    GCD(156,36) = GCD(36,12) = GCD(12, 0) = 12
    '''
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x%y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
