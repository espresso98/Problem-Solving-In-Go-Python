# O(N^2), O(N)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        M = matrix
        n = len(M)
        dp = [float('inf')] + M[0] + [float('inf')]

        for i in range(1, n):
            cur_row = [float('inf')] + M[i] + [float('inf')]
            for j in range(1, n + 1):
                cur_row[j] = cur_row[j] + min(dp[j-1], dp[j], dp[j+1])
            dp = cur_row   # min_path_sum_so_far

        return min(dp)
