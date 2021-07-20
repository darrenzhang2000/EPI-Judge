import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

# def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
#                     # 0 .   1 .   2 
#     def helper(n, start, dest, spare):
#         if n < 1:
#             return
#         helper(n - 1, start, spare, dest)
#         res.append([start, dest])
#         pegs[dest].append(pegs[start].pop())
#         helper(n - 1, spare, dest, start)

#     res = []
#     pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, 3)]
#     helper(num_rings, 0, 1, 2)
#     return res


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    '''
    source, spare, destination
    for the nth ring -> move n - 1 rings from source to spare
    move 1 ring from source to dest

    1 peg:
    move disk from 0 to 1 (source to dest)

    2 pegs:
    move disk from 0 to 2 (source to spare)
    move disk from 0 to 1 (source to dest)
    move disk from 2 to 1 (source to dest)
    '''
                # 0 .     2 .    1
    res = []

    def helper(source, spare, dest, n):
        if n < 1:
            return
        # move disks from p0 to p2, using p1 as spare
        helper(source, dest, spare, n - 1)

        # move disk from p0 to p1
        res.append([source, dest])

        # move disks from p2 to p1, using p0 as spare
        helper(spare, source, dest, n - 1)

        return

    helper(0, 2, 1, num_rings)
    return res



@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
