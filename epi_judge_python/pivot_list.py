import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    if not l:
        return
    lessThanKHead = lessThanKTail = ListNode(None)
    equalToKHead = equalToKTail = ListNode(None)
    moreThanKHead = moreThanKTail = ListNode(None)
    it = l
    while it:
        if it.data < x:
            lessThanKTail.next = it
            lessThanKTail = lessThanKTail.next
        elif it.data == x:
            equalToKTail.next = it
            equalToKTail = equalToKTail.next
        else:
            moreThanKTail.next = it
            moreThanKTail = moreThanKTail.next
        it = it.next
    lessThanKHead = lessThanKHead.next
    equalToKHead = equalToKHead.next
    moreThanKHead = moreThanKHead.next

    newHead, newTail = connectLinkedLists(lessThanKHead, lessThanKTail, equalToKHead, equalToKTail)
    newHead, _ = connectLinkedLists(newHead, newTail, moreThanKHead, moreThanKTail)

    return newHead

def printL(newHead):
    cur = newHead
    while cur:
        cur = cur.next

def connectLinkedLists(head0, tail0, head1, tail1):
    if not head0:
        return head1, tail1
    tail0.next = head1
    tail1.next = None
    return head0, tail1
    

def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
