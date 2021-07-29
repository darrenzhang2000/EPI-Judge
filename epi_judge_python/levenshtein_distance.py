from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    if not A or not B:
        return max(len(A), len(B))

    memo = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for j in range(1, len(B) + 1):
        memo[0][j] = memo[0][j - 1] + 1
    for i in range(1, len(A) + 1):
        memo[i][0] = memo[i - 1][0] + 1
    
    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            cA, cB = A[i - 1], B[j - 1]
            if cA != cB:
                memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + 1
            else:
                memo[i][j] = memo[i-1][j-1]
    return memo[-1][-1] 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
