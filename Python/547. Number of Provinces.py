class Solution:
    # Solution 1: DFS, TC: O(n^2), SC: O(n)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        cnt = 0
        
        def dfs(i):
            for j in range(n):   # n x n matrix
                if isConnected[i][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)
        
        for i in range(n): 
            if i not in seen:
                seen.add(i)
                dfs(i)
                cnt += 1    
        return cnt
    
    # Solution 2: Union Find (Quick Union), TC: O(n^3), SC: O(n)
    # Union and find operations take O(n) time in the worst case
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        self.cnt = n
        
        def find(x):
            while x != root[x]:
                x = root[x]
            return x
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX
                self.cnt -= 1
                
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i,j)
        return self.cnt
            
        
    # Solution 3: Optimized Union Find (Compression path optimization with Union by rank)
    # find optimization: Compression path
    # union optimization: Union by rank. link tree w/smaller rank to tree w/larger rank
    # TC: O(n^2*α(N)), SC: O(n)    
    
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if not isConnected or n == 0:
            return 0
        uf = UnionFind(n)     
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        return uf.count