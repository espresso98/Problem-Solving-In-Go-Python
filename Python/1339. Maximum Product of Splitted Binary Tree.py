# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 10^9 + 7.
# O(N), O(N)
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        max_prod = 0
        all_sums = []

        def tree_sum(node):
            if not node: 
                return 0
            left = tree_sum(node.left)
            right = tree_sum(node.right)
            cur_sum = left+ right + node.val
            all_sums.append(cur_sum)
            return cur_sum
        
        total = tree_sum(root)
        for s in all_sums:
            max_prod = max(max_prod, (total - s) * s)

        return max_prod % (10**9 + 7)
