# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftList = ListNode(0, None)
        rightList = ListNode(0, None)

        cur = head
        l = leftList
        r = rightList
        # l : 0 -> 1 -> 2 ->
        # r : 0 -> 4 -> 3 ->
        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                r.next = cur
                r = r.next
            cur = cur.next
        
        l.next = rightList.next
        r.next = None
        return leftList.next
        