# Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
# O(N), O(1)
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r < len(nums) - 1:
            if (nums[l] < nums[r] and nums[r] > nums[r + 1]) or (
                nums[l] > nums[r] and nums[r] < nums[r + 1]):
                res += 1
                l = r
            r += 1
        return res
