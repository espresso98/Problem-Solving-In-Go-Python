class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative Inorder Traversal
# O(n+k), O(n)
# O(H + k) worst O(N + k) best O(logN + k), O(H) considering callstack where H is a tree height 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node) 
                node = node.left  
            node = stack.pop() 
            k -= 1           
            if k == 0:
                return node.val
            node = node.right
            
        
# Recursive Inorder Traversal
# O(n)/O(H + k), O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        self.k = k
        self.val = None
        self.inorder(root)
        return self.val
    
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.val = node.val
            return
        self.inorder(node.right)

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3