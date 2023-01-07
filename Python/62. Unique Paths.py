# O(M*N), O(M*N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:      
        dp = [[1] * n for i in range(m)]   # [[1, 1], [1, 1], [1, 1]]

        for i in range(1, m):      # down           m = 3, n = 2
            for j in range(1, n):  # right            [1, 1]
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # [1, 2] <- (1,1)
                                                    # [1, 3] <- (2,1)                                   
        return dp[-1][-1]
