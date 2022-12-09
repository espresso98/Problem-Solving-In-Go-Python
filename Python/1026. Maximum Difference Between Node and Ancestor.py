# O(N), O(N)
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def helper(node, cur_max, cur_min):
            if not node: return 

            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            
            if not node.left and not node.right:
                self.res = max(self.res, abs(cur_max - cur_min))
            
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)
            return self.res

        self.res = 0
        return helper(root, root.val, root.val)


class Solution2:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def helper(node, high, low):
            if not node:  # leave node
                return abs(high - low)
            high = max(high, node.val)
            low = min(low, node.val)
            left = helper(node.left, high, low)
            right = helper(node.right, high, low)
            return max(left, right)
        
        return helper(root, root.val, root.val)