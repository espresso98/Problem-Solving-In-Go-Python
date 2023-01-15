# O(NlogN), O(N)
import collections

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # build a graph
        adj = collections.defaultdict(set)  # {0: {1, 2}, 1: {0}, 2: {0, 3, 4}, 3: {2}, 4: {2}}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        # find {val:nodes} mapping
        same_val_nodes = collections.defaultdict(set)  # {1: {0, 3}, 3: {1, 4}, 2: {2}}
        for idx, val in enumerate(vals):
            same_val_nodes[val].add(idx)

        # union-find 
        n = len(vals)             
        root = [i for i in range(n)]    # [0,1,2,3,4]
        rank = [1 for i in range(n)]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        # union by rank, link tree w/smaller rank to tree w/larger rank  
        def union(x, y):  
            rootX, rootY = find(x), find(y)
            if rank[rootX] >= rank[rootY]:
                root[rootY] = rootX
                rank[rootX] += rootY
            else:
                root[rootX] = rootY
                rank[rootY] += rootX

        # find the number of distinct good paths
        res = 0   
        for val in sorted(same_val_nodes.keys()):   # {1: {0, 3}, 2: {2}, 3: {1, 4}}
            for i in same_val_nodes[val]:   # {0, 3}  {2}  {1, 4}
                for j in adj[i]:            # {0: {1, 2}, 1: {0}, 2: {0, 3, 4}, 3: {2}, 4: {2}}
                    if vals[j] <= val:      # Only choose neighbors with a smaller value or equal to the starting node
                        union(i, j)         #         (2,0) (2,3)  1 <= 2   (1,0) 1 <= 3 (4,2) 2 <= 3 

            cnts = collections.Counter()
            for i in same_val_nodes[val]:  # {0, 3}  {2}  {1, 4}
                cnts[find(i)] += 1         # {0: 1, 3: 1}, {2: 1}, {2: 2}
                res += cnts[find(i)]       # 1, 2, 3, 4, 6
        return res