# [Solution1] DP: O(N^2), O(N)
# dp[i] : LIS at index i, nums[i] as the end element of the subsequence
# DP update rule
# if all[j] < all[i] and LIS[i] <= LIS[j]:
#   dp[i] = dp[j] + 1
# nums = [1,3,6,7,9,4,10,5,6]
# LIS  = [1,2,3,4,5,3, 6,4,5]
# [5,8,7,1,9]
# [1,2,2,1,3]
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        LIS = [1] * len(nums) # dp, update LIS[i]
        for i in range(1, len(nums)):
            for j in range(i): # compare nums[j] for all j before i, j = prev
                if nums[j] < nums[i] and LIS[i] <= LIS[j]:
                        LIS[i] = LIS[j] + 1  # or LIS[i] = max(LIS[i], LIS[j] + 1)
            res = max(res, LIS[i])
        return res

# [Solution2] Greedy with Binary search: O(NlogN), O(N)
# bisect_left(arr, x): Locate the insertion point for x in a to maintain sorted order.
# If x is already present in a, the insertion point will be before (to the left of) any existing entries. 
# (1) if x is larger than all tails, append it
# (2) if tails[i-1] < x < tails[i], update tails[i]
from bisect import bisect_left
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for num in nums:
            i = bisect_left(LIS, num)
            print(i)
            if i == len(LIS): #  If num is greater than any element in LIS, just append
                LIS.append(num)
            elif num < LIS[i]:   # replace the first el in LIS which is greater than num
                LIS[i] = num
        return len(LIS)

# [10,9,2,5,3,7,101,18]
# 0 [10]
# 0 [9]
# 0 [2]
# 1 [2, 5]
# 1 [2, 3]
# 2 [2, 3, 7]
# 3 [2, 3, 7, 101]
# 3 [2, 3, 7, 18]
