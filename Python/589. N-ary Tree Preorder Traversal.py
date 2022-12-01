class Solution(object):
    def preorder(self, root):
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root: return
        res.append(root.val)

        for child in root.children:
            print(child.val)
            self.dfs(child, res)

# O(N), O(N)
class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for i in range(len(cur.children)-1, -1, -1):
                stack.append(cur.children[i])
        return res
        