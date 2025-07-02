# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_next = head
        prev = None

        while head:
            tmp_next = head.next
            head.next = prev
            prev = head
            head = tmp_next
        
        return prev
        