# W: wall, E: enemy, 0: empty
# TC: O(m*n), SC: O(n)
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        
        rows, cols = len(grid), len(grid[0])
        max_cnt = 0
        row_hits, col_hits = 0, [0] * cols
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'W':
                    continue
                    
                if col == 0 or grid[row][col-1] == 'W':
                    row_hits = 0 # (re)start scan along the cols
                    for k in range(col, cols):
                        if grid[row][k] == 'W':
                            break # stop the scan when we hit the the wall
                        elif grid[row][k] == 'E':
                            row_hits += 1
                            
                if row == 0 or grid[row-1][col] == 'W':
                    col_hits[col] = 0  # (re)start scan along the rows
                    for k in range(row, rows):
                        if grid[k][col] == 'W':
                            break
                        elif grid[k][col] == 'E':
                            col_hits[col] += 1
                
                if grid[row][col] == '0': # can place the bomb
                    total_hits = row_hits + col_hits[col]
                    max_cnt = max(max_cnt, total_hits)    
                                                   
        return max_cnt
