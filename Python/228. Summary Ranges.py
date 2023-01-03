# O(N), O(1)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0: return []

        res = []
        i = 0
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i+1] == nums[i] + 1:
                i += 1
            if start != nums[i]:
                res.append(f"{start}->{nums[i]}")
            else:
                res.append(f"{start}")
            i += 1
        return res
        