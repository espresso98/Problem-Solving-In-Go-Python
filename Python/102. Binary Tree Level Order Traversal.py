# BFS
# O(n), O(n)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            cur_level = []
            for _ in range(level_size):
                node = q.popleft()
                cur_level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(cur_level)
        return res
            
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]