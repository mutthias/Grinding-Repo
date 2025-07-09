# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        cur = head
        length = 1

        while cur.next:
            cur = cur.next
            length += 1
        
        cur = head
        middle = length // 2
        for _ in range(0, middle):
            cur = cur.next
        
        return cur
        