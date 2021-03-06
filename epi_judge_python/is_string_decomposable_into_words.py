import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        if domain[:i + 1] in dictionary:
            last_length[i] = i + 1
            continue

        for j in range(i):
            if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
                last_length[i] = i - j
                break

    decompositions = []
    if last_length[-1] != -1:
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append(domain[idx + 1 - last_length[idx]:idx + 1])
            idx -= last_length[idx]
        decompositions = decompositions[::-1]
    return decompositions


    # res = []
    # found = [False]
    # def r(domain, res):
    #     if found[0]:
    #         return

    #     for i in range(len(domain)):
    #         prefix = domain[:i + 1]            
    #         if prefix in dictionary: 
    #             res.append(prefix)
    #             suffix = domain[i + 1:]
    #             print(res, prefix, suffix)

    #             if suffix == "":
    #                 found[0] = True
    #                 return
        
    #             r(suffix, res)

    #             res.pop()
            
    # r(domain, res)
    # print(res)
    # return res

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
