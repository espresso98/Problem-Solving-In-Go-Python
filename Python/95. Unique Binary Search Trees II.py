# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start, end):
            if start > end:
                return [None] 
                
            res = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = dfs(start, i - 1)
                # all possible right subtrees if i is choosen to be a root
                right_trees = dfs(i + 1, end)
                # connect left and right subtrees to the root i
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return dfs(1, n)
