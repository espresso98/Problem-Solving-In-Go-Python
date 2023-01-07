# DFS: O(M*N), O(M*N)
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(i,j):
            if 0 <= i < M and 0 <= j < N and grid[i][j] == '1':
                grid[i][j]='#'
                for r, c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    dfs(i+r, j+c)   
                return 1
            return 0

        return sum(dfs(i,j) for i in range(M) for j in range(N))


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(grid,i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] !='1':
                return
            grid[i][j]='#'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)        
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    dfs(grid,i,j)
        return count
    

# BFS: O(M*N), O(max(M,N))
import collections

class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0: 
            return 0
        
        m, n = len(grid), len(grid[0])
        visit = set()
        num = 0
        
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            
            while q:
                row, col = q.popleft()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (nr in range(m) and nc in range(n) and
                        grid[nr][nc] == "1" and (nr,nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))
             
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visit:
                    num += 1
                    bfs(i,j)      
        return num
        