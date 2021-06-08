from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return
    k %= findLength(L)
    if k == 0:
        return L
    dummyHead = ListNode(None, L)
    newTail, it = dummyHead, L
    oldTail = None
    for _ in range(k):
        it = it.next
    while it != None:
        if it.next == None:
            oldTail = it
        it = it.next
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None
    oldTail.next = L
    print(newTail.data, newTail.data)
    return newHead

def findLength(l):
    count = 0
    it = l
    while it:
        count += 1
        it = it.next
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
