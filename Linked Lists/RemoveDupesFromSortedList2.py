# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Idea: iterate, for each node
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq_map = {}
        cur = head

        while cur:
            freq_map[cur.val] = freq_map.get(cur.val, 0) + 1
            cur = cur.next
        
        new_list = ListNode(0, None)
        cur = head
        cur_new = new_list

        while cur:
            if freq_map[cur.val] == 1:
                newNode = ListNode(cur.val, None)
                cur_new.next = newNode
                cur_new = cur_new.next
            cur = cur.next
        
        return new_list.next
                

        