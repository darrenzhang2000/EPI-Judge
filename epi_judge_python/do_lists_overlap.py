import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from do_terminated_lists_overlap import overlapping_no_cycle_lists

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    '''
    - if one ll has a cycle and th other doesn't, then they're not overlapping.
    - if each list have their own individual cycles, then they're not overlapping.
    - if both lists share the same cycles, then they're overlapping.
        - i can return any node in the cycle. once in cycle, use slow pointer, fast pointer approach

    '''
    if not l0 or not l1:
        return

    cycleEntryL0 = has_cycle(l0)
    cycleEntryL1 = has_cycle(l1)
    # if one has a cycle and the other doesn't, no overlap
    if (cycleEntryL0 == None) ^ (cycleEntryL1 == None):
        return None

    # no cycle case
    if not cycleEntryL0 and not cycleEntryL1:
        return overlapping_no_cycle_lists(l0, l1)
    

    # both have cycles.
    it0, cycleLen0 = cycleEntryL0
    it1, cycleLen1 = cycleEntryL1
    for _ in range(max(cycleLen0, cycleLen1)):
        if it0 is it1:
            return it0
        it0 = it0.next
        it1 = it1.next.next



def has_cycle(head: ListNode) -> Optional[ListNode]:
    slow, fast = head, head.next
    while fast != None:
        if fast is slow: # cycle found 
            break
        slow = slow.next
        fast = fast.next.next if fast.next else None

    if fast == None:
        return None

    # find cycle length
    cycleLength = 0
    while True:
        slow = slow.next
        fast = fast.next.next
        cycleLength += 1
        if slow is fast:
            break
    cycleIt = head
    for _ in range(cycleLength):
        cycleIt = cycleIt.next 
    # d = p + c. now cycle it is p steps behind the start of cycle, where p is distance from head to start of cycle

    startIt = head
    while not startIt is cycleIt:
        startIt = startIt.next
        cycleIt = cycleIt.next
    return startIt, cycleLength  


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
