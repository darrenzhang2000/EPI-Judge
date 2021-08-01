from test_framework import generic_test
import functools

def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    '''
    n = 5, k = 3

    r(5) = r(4) + r(3) + r(2)
    r(4) = r(3) + r(2) + r(1)
    r(3) = r(2) + (1) + r(0)

    '''
    @functools.lru_cache
    def r(n, k):
        if n < 0:
            return 0
        if n <= 1:
            return 1
        total = 0
        for i in range(1, maximum_step + 1):
            total += r(n - i, k)
        return total
    
    return r(top, maximum_step)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
