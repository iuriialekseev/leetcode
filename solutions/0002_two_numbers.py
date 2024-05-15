# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        rem = 0

        while l1 != None or l2 != None or rem != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + rem
            rem = sum // 10

            node = ListNode(sum % 10)
            curr.next = node
            curr = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
