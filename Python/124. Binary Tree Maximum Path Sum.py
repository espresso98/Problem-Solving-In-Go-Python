# max_path_sum = max(max_path_sum, left_gain + right_gain + root.val)
# O(n), O(n)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def tree_path_sum(node):
            if not node: return 0
            left = max(tree_path_sum(node.left), 0)
            right = max(tree_path_sum(node.right), 0)
            cur_max_sum = left + right + node.val
            self.max_path_sum = max(self.max_path_sum, cur_max_sum)
            # print(left, right, node.val, cur_max_sum, self.max_path_sum)
            return max(left, right) + node.val

        self.max_path_sum = -math.inf
        tree_path_sum(root)
        return self.max_path_sum 
