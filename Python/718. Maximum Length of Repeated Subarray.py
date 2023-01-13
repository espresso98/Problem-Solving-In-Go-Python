# 1143. Longest Common Subsequence
# # LCS, O(M*N), O(M*N)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            j    0 1 2 3 4 5
          i        3 2 1 4 7 
         -------------------
          0    | 0 0 0 0 0 0
          1  1 | 0 0 0 1 0 0  
          2  2 | 0 0 1 0 0 0
          3  3 | 0 1 0 0 0 0
          4  2 | 0 0 2 0 0 0
          5  1 | 0 0 0 3 0 0
        """

        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)] 
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
        return res


# LCS, O(M*N), O(min(M,N))
class Solution2:     
     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):  # use the shorter string as a dp column
            nums1, nums2 = nums2, nums1  
        m, n = len(nums1), len(nums2)
        res = 0 
        prev = [0] * (n+1)
        for i in range(1, m+1):
            dp = [0] * (n+1)  # current column
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = prev[j-1] + 1
                res = max(res, dp[j])
            prev = dp
        return res
