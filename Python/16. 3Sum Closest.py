# TC: O(n^2), SC: O(logn) to O(n) depending on the implementation of the sorting algorithm.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # [-4, -1, 1, 2] 
        min_diff = float('inf')    # target - closest_sum

        for i in range(len(nums)):
            lo, hi = i + 1, len(nums)-1
            while lo < hi:
                three_sum = nums[i] + nums[lo] + nums[hi]
                cur_diff = target - three_sum
                if abs(cur_diff) < abs(min_diff):
                    min_diff = cur_diff
                if cur_diff < 0:    # target < three_sum
                    hi -= 1
                elif cur_diff > 0:  # target > three_sum
                    lo += 1
                else:               # target == three_sum
                    return three_sum

        closest_sum = target - min_diff
        return closest_sum
        