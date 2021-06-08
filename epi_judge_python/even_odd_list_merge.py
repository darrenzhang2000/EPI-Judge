from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next:
        return L
    evenHead = evenTail = L
    oddHead = oddTail = L.next
    even = True
    it = oddHead.next
    while it:
        if even:
            evenTail.next = it
            evenTail = evenTail.next
        else:
            oddTail.next = it
            oddTail = oddTail.next
        it = it.next
        even = not even
    evenTail.next = oddHead
    oddTail.next = None
    return evenHead


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
