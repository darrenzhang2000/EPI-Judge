from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    res = []
    i = 0
    while i < len(s):
        # get next num
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        num = s[i:j]
        i = j 

        # get next string
        while j < len(s) and s[j].isalpha():
            j += 1
        alpha = s[i:j]
        res.append(int(num) * alpha)
        i = j
    return "".join(res)


def encoding(s: str) -> str:
    res = []
    i = 0
    while i < len(s):
        # get same char
        j = i + 1
        while j < len(s) and s[i] == s[j]:
            j += 1
        count = j - i
        res.append(str(count) + s[i])
        i = j
    return "".join(res)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
