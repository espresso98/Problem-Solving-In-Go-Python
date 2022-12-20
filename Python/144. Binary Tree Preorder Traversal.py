# O(N), O(N)  Root -> L -> R
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], [root]
        
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                if curr.right:  
                    stack.append(curr.right) 
                if curr.left:
                    stack.append(curr.left) 
        return res

        # res = []

        # def dfs(curr:TreeNode) -> None:
        #     if not curr: return
        #     res.append(curr.val)
        #     dfs(curr.left)
        #     dfs(curr.right)
        
        # dfs(root)
        # return res
        