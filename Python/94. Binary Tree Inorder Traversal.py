# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(N), O(N) L -> Root -> R
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        stack = []
        cur_node = root
        while cur_node or stack:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                res.append(cur_node.val)
                cur_node = cur_node.right
        return res

        # recursion
        # res = []
        
        # def helper(node):
        #     if not node: return
        #     helper(node.left)
        #     res.append(node.val)
        #     helper(node.right)
            
        # helper(root)
        # return res
