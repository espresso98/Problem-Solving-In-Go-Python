# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# DFS
# Time complexity: O(N)  becasue we visit every node once. 
# Space complexity: O(N) because the size of call stack during dfs
class Solution:
    # Solution1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # unbalanced = -1
        def getHeight(node):
            if not node: return 0
            left = getHeight(node.left) 
            right = getHeight(node.right) 
            if left == -1 or right == -1: 
                return -1
            if abs(left-right) > 1:  
                return -1
            return max(left,right) + 1
        return getHeight(root) != -1

    # Solution2
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: 
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
    
# Input: root = [3,9,20,null,null,15,7]
# Output: true
