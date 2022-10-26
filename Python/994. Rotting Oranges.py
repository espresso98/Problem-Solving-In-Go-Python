# 0: empty cell
# 1: fresh orange
# 2: rotten orange

# TC: O(m*n) size of the grid. SC: O(m*n) size of the queue
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        rotten = deque()  # BFS: keep track of the candidates that we need to visit during the process.
        # step 1. build the initial set of rotten oranges and count the fresh oranges 
        M, N = len(grid), len(grid[0])
        for r in range(M):
            for c in range(N):
                # update fresh oranges count
                if grid[r][c] == 1:
                    fresh += 1
                # add the rotten orange coordinates to the queue
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        print(rotten)  # deque([(0, 0)])
        
        if not fresh: # no fresh orange
            return 0
        elif not rotten: # no rotten orange
            return -1
        
        # step 2. start the rotting process via BFS
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while rotten and fresh > 0:
            # print(rotten)
            # update the number of minutes elapsed
            time += 1  # level in BFS
            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                r, c = rotten.popleft()   
                # visit all the adjacent cells
                for dr, dc in dirs:
                    # calculate the coordinates of the adjacent cell
                    row, col = r + dr, c + dc
                    # print(row, col)
                    # if in bounds and nonrotten, make rotten and add to queue
                    if row in range(M) and col in range(N) and grid[row][col] == 1:
                        # mark the current fresh orange as rotten
                        grid[row][col] = 2   
                        rotten.append((row, col))
                        # update the fresh oranges count
                        fresh -= 1
            
        # return the number of minutes taken or -1 if there are fresh oranges left in the grid
        return time if not fresh else -1