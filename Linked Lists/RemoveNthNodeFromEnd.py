# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:    
        nextNode = head
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        
        # 5 4 3 2 1
     
        curNode = prev
        prevNode = None
        for i in range(0, n - 1):
            prevNode = curNode
            curNode = curNode.next

        if prevNode == None:
            prev = curNode.next
        else:
            prevNode.next = curNode.next

        second_prev = None
        second_next = prev
        
        while prev:
            second_next = prev.next
            prev.next = second_prev
            second_prev = prev
            prev = second_next
        
        return second_prev


        