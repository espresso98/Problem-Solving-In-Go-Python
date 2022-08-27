# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
        
#     # O(nlgn) / O(1) or O(n)   
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums)//2]
    
#     # O(n) / O(n)
#     def majorityElement(self, nums):
#         m = {}
#         for n in nums:
#             m[n] = m.get(n, 0) + 1
#             if m[n] > len(nums)//2:
#                 return n
        
    # Boyer-Moore Voting Algorithm: O(n) / O(1)   
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            #print(candidate, count)        
        return candidate
        
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

