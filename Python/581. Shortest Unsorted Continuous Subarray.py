# [1,3,2,2,2] => 4
# [1, 3, 7, 2, 5, 4, 6, 10], where l = 2, r = 5, subarray= [7, 2, 5, 4]
# include 3 on the left and 6 on the right

# TC: O(N), SC: O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        # first non-ascending, first non-descending
        l, r = 0, len(nums) - 1
        while l < len(nums)-1 and nums[l] <= nums[l+1]:
            l += 1
        while r > 0 and nums[r-1] <= nums[r]:
            r -= 1
        if r < l: return 0 # everything is sorted
          
        subarray = nums[l:r+1]
        sub_min, sub_max = min(subarray), max(subarray)

        while l > 0 and nums[l-1] > sub_min:
            l -= 1
        while r < len(nums)-1 and nums[r+1] < sub_max:
             r += 1

        return r - l + 1
                