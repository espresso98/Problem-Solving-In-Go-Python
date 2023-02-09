# 53. Maximum Subarray
# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = sub_sum = nums[0] 
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                sub_sum += nums[i]
            else:
                sub_sum = nums[i]
            max_sum = max(max_sum,sub_sum)
        return max_sum
        