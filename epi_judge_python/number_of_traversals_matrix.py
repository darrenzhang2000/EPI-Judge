from test_framework import generic_test
import math
import functools
def number_of_ways(n: int, m: int) -> int:
    '''
    n - 1 downs
    m - 1 rights
    (m + n - 2) choose (m - 1)
    return math.factorial(n - 1 + m - 1) // (math.factorial(n - 1) * math.factorial(m - 1))
    '''

    '''
    @functools.lru_cache
    def count_ways(n, m):
        if n <= 1 or m <= 1:
            return 1
        from_left = count_ways(n, m - 1)
        from_up = count_ways(n - 1, m)
        return from_left + from_up

    return count_ways(n, m)
    '''
    memo = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[-1][-1]


    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
