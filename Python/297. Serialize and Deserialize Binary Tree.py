# Preorder DFS (root -> left subtree -> right subtree)
# O(n), O(n)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        
        def dfs(node):
            if not node: 
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(vals)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if self.i == len(vals):
                return None  
            
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            val = int(vals[self.i])
            node = TreeNode(val)
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
