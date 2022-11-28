# Input: nums = [2,7,9,3,1]
# Output: 12
# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max(f(k-1), f(k-2) + nums[k])
# dp[0]    dp[1]     dp[2]      dp[3]      dp[4]
#   2     2 or 7   7 or 2+9  11 or 7+3   11 or 11+1

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution1. TC: O(N), SC: O(N)
        if not nums: return 0
        if len(nums) < 3: return max(nums)

        dp = [0]*len(nums)
        dp[0], dp[1] = nums[0], max(nums[0],nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
        return dp[-1]


        # Solution 2. TC: O(N), SC: O(1)
        prev, cur = 0, 0
        for n in nums: 
            prev, cur = cur, max(prev + n, cur)  
        return cur
