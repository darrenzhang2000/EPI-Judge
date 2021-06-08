from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(l1: Optional[ListNode],
                           l2: Optional[ListNode]) -> Optional[ListNode]:
    newHead = ListNode()
    cur = newHead
    n1, n2 = l1, l2
    while n1 or n2:
        v1 = n1.data if n1 else float('inf')
        v2 = n2.data if n2 else float('inf')
        if v1 < v2:
            cur.next = n1 
            n1 = n1.next
        else:
            cur.next = n2
            n2 = n2.next
        cur = cur.next
    return newHead.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
