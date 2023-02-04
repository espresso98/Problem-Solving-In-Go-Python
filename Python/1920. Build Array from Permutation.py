# O(n) / O(n)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[n] for n in nums]  # val-> idx
        
# O(n) / O(1) 
class Solution2:
    def buildArray(self, nums: List[int]) -> List[int]:
        return (nums[n] for n in nums)  # generator comprehension