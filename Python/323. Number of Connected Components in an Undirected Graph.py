# Solution 1: DFS, TC: O(V+E), SC: O(V+E)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        def dfs(node):
            seen.add(node)
            for nb in adj[node]:
                if nb not in seen:
                    dfs(nb)
        count = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                dfs(node)
                count += 1
        return count

# Solution 2: Union Find, TC: O(V+E⋅α(V)) ≈ O(V+E), SC: O(V)
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
           
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX            
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX                    
                self.rank[rootX] += 1
            self.count -= 1
      
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)  
        for a, b in edges:
            uf.union(a,b)       
        return uf.count