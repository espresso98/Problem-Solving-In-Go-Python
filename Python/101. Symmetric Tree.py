# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N), O(N)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(n1, n2):   # dfs
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            return is_mirror(n1.right, n2.left) and is_mirror(n1.left, n2.right)        
        return is_mirror(root.left, root.right)

# Input: root = [1,2,2,3,4,4,3]
# Output: true
