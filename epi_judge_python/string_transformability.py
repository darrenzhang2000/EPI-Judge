from typing import Set
import collections
import string
from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    '''
    brute force:
    go through the s string,
        go thru all letters of alphabet
            check if new string exists in set, then call recursive algorithm
    O(s!)

    optimized soln:
    build a undirected graph where each edge seperates two vertices with exactly one letter difference
    check if it's possible to reach vertex s to vertex t
    O(v+e) 
    '''
    if len(s) != len(t):
        return False

    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)

    while q:
        f = q.popleft()
        if f.candidate_string == t:
            return f.distance
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1
    



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
