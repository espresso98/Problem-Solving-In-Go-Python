# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Traversal with Valid Range
# O(n), O(n)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lower= float('-inf'), upper=float('inf')):
            if not node: return True
            if not (node.val > lower and node.val < upper): 
                return False
            return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)
        return validate(root)
                