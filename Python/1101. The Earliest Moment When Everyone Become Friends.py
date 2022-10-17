# TC: O(V + ElogE + E*α(V)) ≈ O(V+ElogE), SC: O(V+E)  where V is the number of people and E is the number of log
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n) 
        logs.sort(key = lambda x : x[0])
        for t, u, v in logs:
            uf.union(u,v)
            if uf.count == 1:
                return t
        return -1