from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t): return -1

    n = len(s)
    sHash = computeHash(s, 0, n)
    curHash = computeHash(t, 0, n)
    for i in range(n - 1, len(t) - 1):
        startIdx = i - len(s) + 1
        if curHash == sHash:
            return startIdx
        curHash = 37 * (curHash - ord(t[startIdx]) * 37 ** (n - 1)) + ord(t[i + 1])
    # compute hash once more
    if curHash == sHash:
        return len(t) - n
    return -1

def computeHash(s, start, end):
    n = 0
    for i in range(start, end):
        n = 37 * n + ord(s[i])
    return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
