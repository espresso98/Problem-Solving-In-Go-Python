class Solution:
    # Solution 1: DFS, TC: O(N+E), SC: O(N+E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:       
        if len(edges) != n-1:
            return False
        # create an adjacency list
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        # print(adj)    
        seen = set()
        
        def dfs(node):
            if node in seen: 
                return False
            seen.add(node)
            for nb in adj[node]:
                dfs(nb)
        dfs(0)
        # the entire graph has been reached
        return len(seen) == n

# Solution 2: DFS, TC: O(N*α(N)), SC: O(N)
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
        
    # The find function with path compression
    def find(self, x):
            if x == self.root[x]:
                return x
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        
    # The union function with union by rank    
    def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            # check if X and Y are already in the same set
            if rootX == rootY:
                return False
            else:
                if self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1
                self.count -= 1
            return True        

class Solution:        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:       
        if len(edges) != n-1:
            return False
        uf = UnionFind(n)  
        for a, b in edges:
            if not uf.union(a,b): # cycle detection
                return False
        return uf.count == 1  # fully connected and no cycle