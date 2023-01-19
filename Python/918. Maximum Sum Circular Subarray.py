# Kadane's Algorithm: O(N) finding the maximum sum subarray from a given array
# max(prefix + suffix)
# = max(total_sum - subarray)
# = total_sum - min(subarray)
# O(N), O(1)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = cur_min = 0
        max_sum = min_sum = nums[0]

        # noncircular_max_sum: Kadane's Algorithm(maximum_sum subarray)
        for num in nums:
            cur_max = max(cur_max, 0) + num
            max_sum = max(max_sum, cur_max)

        # circular_max_sum: max(prefix + suffix) = total_sum - min(subarray)
        for num in nums:
            cur_min = min(cur_min, 0) + num
            min_sum = min(min_sum, cur_min)  
        circular_sum = sum(nums) - min_sum 

         # If all numbers are negative sum(nums) = min_sum, circular_sum = 0
         # return max_sum = max(nums) < 0
        return max_sum if max_sum <= 0 else max(max_sum, circular_sum) 


class Solution2:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # If all numbers are negative return max(nums)
        if all(num < 0 for num in nums): 
            return max(nums)

        cur_max = cur_min = max_sum = min_sum = nums[0]
        for num in nums[1:]:
            # noncircular_max_sum: Kadane's Algorithm(maximum_sum subarray)
            cur_max = max(cur_max, 0) + num
            max_sum = max(max_sum, cur_max)
            # circular_max_sum: max(prefix + suffix) = total_sum - min(subarray)
            cur_min = min(cur_min, 0) + num
            min_sum = min(min_sum, cur_min)   

        return max(max_sum, sum(nums) - min_sum) 
        