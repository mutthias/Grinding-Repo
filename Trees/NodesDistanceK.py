# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        
        graph = defaultdict(list)

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)

        res = []
        visited = set([target])

        bfs_queue = deque([(target, 0)])

        while bfs_queue:
            node, distance = bfs_queue.popleft()
            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        bfs_queue.append((edge, distance + 1))

        return res

            
        