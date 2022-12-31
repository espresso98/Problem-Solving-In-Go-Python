# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
# O(3^N), O(N)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_r, start_c, end_r, end_c = 0, 0, 0, 0
        empty = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 2:
                    end_r, end_c = r, c
                elif grid[r][c] == 0:
                    empty += 1

        self.res = 0
        visited = set()
        def dfs(r,c,visited,walk):
            if r == end_r and c == end_c:
                if walk == empty + 1:
                    self.res += 1
                return

            if 0 <= r < m and 0 <= c < n and grid[r][c] != -1 and (r,c) not in visited:
                visited.add((r,c))
                for i, j in [(0,-1),(0,1),(-1,0),(1,0)]:
                    dfs(r+i,c+j,visited,walk+1)
                visited.remove((r,c))

        dfs(start_r,start_c,visited,0)
        return self.res
