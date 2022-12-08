# Recursive DFS (Pre-order): O(root1 + root2), O(root1 + root2)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(node):
            if not node: return []
            if not node.left and not node.right:
                return [node.val]
            return leaves(node.left) + leaves(node.right)
        return leaves(root1) == leaves(root2)

# Iterative DFS (Pre-order)
class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(node):
            if not node: return 
            st, leaf = [node], []
            while st:
                node = st.pop()
                if not node.left and not node.right:
                    leaf.append(node.val)
                if node.right:
                    st.append(node.right)
                if node.left:
                   st.append(node.left)
            return leaf
        return leaves(root1) == leaves(root2)
