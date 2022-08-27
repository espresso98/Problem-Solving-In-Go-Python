# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
#The length of a path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# Time complexity: O(N)  becasue we visit every node once. 
# Space complexity: O(N) because the size of call stack during dfs

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0  # the length of the longest path
        def get_depth(node):
            nonlocal res
            if not node: return 0
            left = get_depth(node.left)
            right = get_depth(node.right)
            # update the longest path
            res = max(res, left + right)
            # print(node.val, res, max(left, right) + 1)
            return max(left, right) + 1
        get_depth(root)
        return res 

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].