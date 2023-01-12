# Number of Nodes in the Sub-Tree With the Same Label
# Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.
# labels = "abaedcd"
# O(N), O(N)
import collections

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent=None):
            counter = collections.Counter() # subtree counter
            for child in adj[node]:
                if child == parent: continue
                counter += dfs(child, node)   

            counter[labels[node]] += 1        # {'a': 1}
            res[node] = counter[labels[node]] # [0, 0, 0, 1, 0]
            return counter   # counter = {'a': 3, 'b': 2}), res = [3, 2, 1, 1, 1]
        
        res = [0] * n
        dfs(0)
        return res

# n = 5
# edges = [[0,1],[0,2],[1,3],[0,4]]
# labels = "aabab"
# Expected [3,2,1,1,1]

# adj: {0: [1, 2, 4], 1: [0, 3], 2: [0], 3: [1], 4: [0]})
# Counter({'a': 1}) [0, 0, 0, 1, 0]
# Counter({'a': 2}) [0, 2, 0, 1, 0]
# Counter({'b': 1}) [0, 2, 1, 1, 0]
# Counter({'b': 1}) [0, 2, 1, 1, 1]
# Counter({'a': 3, 'b': 2}) [3, 2, 1, 1, 1]
