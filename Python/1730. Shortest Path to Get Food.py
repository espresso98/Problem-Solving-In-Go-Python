# BFS: O(M*N), O(M*N)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        for row in range(R):
            for col in range(C):
                if grid[row][col] == '*':
                    queue.append((row, col, 0))
                    visited.add((row, col))
                    break
        
        dirs = [(1,0), (-1,0), (0,-1), (0, 1)]
        while queue:               
            cur_row, cur_col, steps = queue.popleft()
            if grid[cur_row][cur_col] == '#':
                return steps
            else:
                for r_dir, c_dir in dirs:
                    new_row, new_col = cur_row + r_dir, cur_col + c_dir
                    if (0 <= new_row < R) and (0 <= new_col < C) and grid[new_row][new_col] != 'X':
                        if (new_row, new_col) not in visited:
                            queue.append((new_row, new_col, steps + 1))
                            visited.add((new_row, new_col))

        return -1
