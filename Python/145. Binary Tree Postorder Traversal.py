from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N), O(N)   L -> R -> Root 
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        res, stack = [], [root]
 
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val) # Root -> R -> L
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return res[::-1] # L -> R -> Root
        
        # return reversed(res)

        # res = []
        # def dfs(node):
        #     if not node: return
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        # dfs(root)
        # return res
