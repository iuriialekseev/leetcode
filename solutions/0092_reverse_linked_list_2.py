from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        pos = 0
        prev = None
        curr = head

        while curr:
            if pos >= left and pos <= right:
                next = curr.next
                prev.next = next
                curr.next = prev

            prev = curr
            curr = curr.next
            pos += 1

        return head
