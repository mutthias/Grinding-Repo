# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3 4 5
# 5 4 3 2 1
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev, cur = dummy, head

        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
        
        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next
        