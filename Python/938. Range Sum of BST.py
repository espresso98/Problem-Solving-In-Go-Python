# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1. Recursive DFS (Inorder): O(N), O(H)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node: return 0
            if low <= node.val <= high:
                self.res += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        self.res = 0
        dfs(root)
        return self.res

    # Solution 2. Iterative DFS (Inorder): O(N), O(H)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        st = [root]
        while st:
            node = st.pop()
            if low <= node.val <= high:
                res += node.val
            if node.left and node.val > low:
                st.append(node.left)
            if node.right and node.val < high:
                st.append(node.right)
        return res
        