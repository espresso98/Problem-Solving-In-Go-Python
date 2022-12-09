# O(N), O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
        return -1
