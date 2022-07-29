class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# iteratvie: O(logN), O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None      
        cur = root
        while cur:
            # print(cur.val)
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left 
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                 return cur
        