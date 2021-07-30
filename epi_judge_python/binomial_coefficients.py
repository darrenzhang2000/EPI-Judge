from test_framework import generic_test
import functools

@functools.lru_cache
def compute_binomial_coefficient(n: int, k: int) -> int:
    '''
    nCk = 

    5 balls, choose 3 red ball
    4 balls, choose red + 4 balls, don't choose red
    '''
    if n == k or k == 0:
        return 1

    not_pick = compute_binomial_coefficient(n - 1, k)
    pick = compute_binomial_coefficient(n - 1, k - 1)

    return not_pick + pick

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
