import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    '''
    first sort
    keep appending until overlap is found
    while overlap, keep taking union
    append the rest
    '''

    disjoint_intervals.sort()
    res = []

    # stage 1
    i = 0
    while i < len(disjoint_intervals):
        interval = disjoint_intervals[i]
        if interval.right < new_interval.left: # no overlap
            res.append(interval)
            i += 1
        else:
            break

    # stage 2
    union_interval = new_interval
    while i < len(disjoint_intervals):
        interval = disjoint_intervals[i]
        if union_interval.right < interval.left: # no more overlap
            break
        new_left = min(union_interval.left, interval.left)
        new_right = max(union_interval.right, interval.right)
        union_interval = Interval(new_left, new_right)
        i += 1
    res.append(union_interval)

    # stage 3
    while i < len(disjoint_intervals):
        interval = disjoint_intervals[i]
        res.append(interval)
        i += 1

    return res 


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
