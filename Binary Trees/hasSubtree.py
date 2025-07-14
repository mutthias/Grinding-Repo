# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False            
        
        q = deque()
        q.append(root)

        def isSameTree(r1, r2):
            if not r1 and not r2:
                return True
            if r1 and r2 and r1.val == r2.val:
                return isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)
            else:
                return False
        
        while q:
            node = q.popleft()
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
                

        
        