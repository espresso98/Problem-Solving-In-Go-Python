# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

class Solution:
    # DFS approach
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, seen):
            if root == None: return False
            complement = k - root.val
            if complement in seen: return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        
        return dfs(root, set())

    # BFS approach
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack, seen = [root], set()
        while stack:
            node = stack.pop()  
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
