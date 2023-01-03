class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(filter(lambda x: x > 0, nums)))
        # return len(set(nums) - {0})
        