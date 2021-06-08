from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    '''
    1 -> 2 -> 3
    |
              |
    to delete the second to last element, have the slow ptr be 2 ahead
    of the fast ptr. when the fast ptr is null, the node is found

    assume that k is valid
    '''
    slow = fast = L
    for _ in range(k):
        fast = fast.next
    if not fast: # first node has to be deleted
        L = L.next
        return L
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next if slow.next else None
    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
