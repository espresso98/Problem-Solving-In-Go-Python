# Find the minimum prefix sum.
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
# O(N), O(1)
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum, min_sum = 0, 0
        for n in nums:
            prefix_sum += n
            min_sum = min(min_sum, prefix_sum) 
        # if min_sum >= 0 :
        #     return 1  # Minimum start value should be positive
        # else: 
        return 1 - min_sum
        