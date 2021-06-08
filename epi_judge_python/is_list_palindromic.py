from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True
    steps = 0
    slow = fast = L
    while fast and fast.next:
        steps += 1
        slow = slow.next
        fast = fast.next.next

    # reverse second half of linked list
    prev = slow
    cur = slow.next
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    h2 = prev
    h1 = L
    for _ in range(steps):
        if h1.data != h2.data:
            return False
        h1 = h1.next
        h2 = h2.next
    return True




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
