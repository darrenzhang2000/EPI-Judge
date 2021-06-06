import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    s.reverse()
    start, end = 0, 0
    while True:
        try:
            end = s.index(" ", start, len(s))
        except ValueError:
            break
        reverseWord(s, start, end)
        start = end + 1
    reverseWord(s, start, len(s))
    return s

def reverseWord(s, start, end):
    for i in range((end - start) // 2):
        s[start + i], s[end - 1 - i] = s[end - 1 - i], s[start + i]

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
