from collections import deque 
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Solutoin 1. Recursive DFS(Pre-order): O(N), O(H)
        def dfs(node, isLeft):
            if not node: return 0
            if not node.left and not node.right: # leaf
                return node.val if isLeft else 0
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)

        # Solutoin 2. Iterative DFS(Pre-order): O(N), O(H)
        st, res = deque([(root, False)]), 0
        while st:
            cur, isLeft = st.pop()
            if not cur.left and not cur.right and isLeft:
                res += cur.val
            else: 
                if cur.right: 
                    st.append((cur.right, False))
                if cur.left: 
                    st.append((cur.left, True))
        return res

        # Solutoin 3. BFS: O(N), O(W)
        q, res = deque([(root, False)]), 0
        while q:
            cur, isLeft = q.popleft()
            if not cur.left and not cur.right and isLeft:
                res += cur.val
            else: 
                if cur.right: 
                    q.append((cur.right, False))
                if cur.left: 
                    q.append((cur.left, True))
        return res
