from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev
