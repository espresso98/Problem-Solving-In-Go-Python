# Solution 1: O(M*N), O(M*N)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        lcs = ""
        for i in range(1, m + 1): 
            for j in range(1, n + 1):  
                if text1[i-1] == text2[j-1]:
                    lcs += text1[i-1]
                    dp[i][j] = 1 + dp[i-1][j-1]  
                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # print("i/j")
        # for i in range(m+1):
        #     print(dp[i])
        # print(f"\nThe LCS is: '{lcs}'")
        
        return dp[m][n]

# Solution2: O(M * N), O(MIN(M,N))
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)
        lcs = ""

        for i in range(1, m + 1): 
            for j in range(1, n + 1):  
                if text1[i-1] == text2[j-1]:
                    lcs += text1[i-1]
                    cur[j] = 1 + prev[j-1]  
                else: 
                   cur[j] = max(cur[j-1], prev[j])                    
            cur, prev = prev, cur
        print(lcs)  
        return prev[n]
