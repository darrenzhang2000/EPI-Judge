from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# def reverse_sublist(L: ListNode, start: int,
#                     finish: int) -> Optional[ListNode]:
#     if start == finish:
#         return L
    
#     head = L
#     for _ in range(1, start):
#         head = head.next
#     beforeHead = L if head == L else None
#     while beforeHead and beforeHead.next != head:
#         beforeHead = beforeHead.next

#     tail = L
#     for _ in range(1, finish):
#         tail = tail.next
#     afterTail = tail.next
#     print(tail.data)


#     reverseLinkedList(beforeHead, head, tail, afterTail)
#     return L if start != 1 else tail

# def reverseLinkedList(beforeHead, head, tail, afterTail):
#     prev = head
#     cur = head.next
#     while cur != tail:
#         temp = cur.next
#         cur.next = prev
#         prev = cur 
#         cur = temp
#     cur.next = prev
#     if beforeHead:
#         beforeHead.next = tail
#     head.next = afterTail
    

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if start == finish:
        return L
    beforeNode = getNthNode(L, start - 1) if start != 1 else None
    oldHead = beforeNode.next if beforeNode else L
    oldTail = getNthNode(L, finish)
    afterNode = oldTail.next
    newHead, newTail = reverseLinkedList(oldHead, oldTail)
    # reattach nodes
    if beforeNode:
        beforeNode.next = newHead
    newTail.next = afterNode # afterNode could be null
    return L if start != 1 else newHead

def reverseLinkedList(head, tail):
    newHead = tail
    newTail = head
    prev = head
    cur = head.next
    while prev != tail:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        if prev.data == tail.data:
            break
    return newHead, newTail
        

    

def getNthNode(L, n):
    cur = L
    for _ in range(1, n):
        if not cur:
            return None
        cur = cur.next
    return cur

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
