# A square matrix is said to be an X-Matrix if both of the following conditions hold:
# All the elements in the diagonals of the matrix are non-zero. All other elements are 0.
# Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.

# Time Complexity:  O(n^2),  Space Complexity: O(1)
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                # diagonal
                if i == j or (i + j == n-1):
                    if grid[i][j] == 0:
                        return False
                # non-diagnonal
                elif grid[i][j] != 0:
                    return False
        return True