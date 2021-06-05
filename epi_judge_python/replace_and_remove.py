import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    removeBs(size, s)
    replaceAs(size, s)
    return s

def removeBs(size, s):
    slow = fast = 0
    while fast < size:
        if s[fast] != 'b':
            s[slow] = s[fast]
            slow += 1
        fast += 1
    for i in range(slow, size):
        s[i] = None
    
def replaceAs(size, s):
    if None not in s: # no 'a's
        return 
    lastElIdx = s.index(None) - 1 
    indexCopyTo = size - 1
    for i in range(lastElIdx, -1, -1):
        if s[i] == 'a':
            s[indexCopyTo - 1: indexCopyTo + 1] = ['d', 'd']
            indexCopyTo -= 2
        else:
            s[indexCopyTo] = s[i]
            indexCopyTo -= 1
            


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
