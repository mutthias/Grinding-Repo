"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_hash = { None : None }
        
        cur = head
        while cur:
            newNode = Node(cur.val)
            node_hash[cur] = newNode
            cur = cur.next
        
        cur = head
        while cur:
            newNode = node_hash[cur]
            newNode.next = node_hash[cur.next]
            newNode.random = node_hash[cur.random]
            cur = cur.next

        return node_hash[head]
        