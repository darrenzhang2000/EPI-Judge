import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    '''
    first sort events based on starting time. 
    for each event, find the other events whose start times are less than this event's end time
        - this marks an overlap
        - count overlaps
        - this is inefficient because going to every point in the interval takes way too long

    bottle neck - checking every point in the interval
    - instead of checking every point in the interval, just check the starting and ending point
    - each starting point increases the overlap counter by one
    - each ending point decreases the overlap count by one

    - extract all starting and endpoint points. then implement above algorithm
    - time complexity: O(nlogn), space o(n)
    '''
    critical_points = []
    for e in A:
        critical_points.append((e.start, '1start'))
        critical_points.append((e.finish, '2finish'))

    critical_points.sort()
    max_overlap = 0
    overlap_counter = 0
    for n, typ in critical_points:
        if typ == '1start':
            overlap_counter += 1
        else:
            overlap_counter -= 1
        max_overlap = max(max_overlap, overlap_counter)

    return max_overlap



@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
