# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        cur = head
        length = 1

        while cur.next:
            cur = cur.next
            length += 1
        
        k = k % length

        if k == 0:
            return head
        
        tail = cur
        cur = head

        for i in range(length - k - 1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead
        
