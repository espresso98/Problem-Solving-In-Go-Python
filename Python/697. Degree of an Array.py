# The degree of this array is defined as the maximum frequency of any one of its elements.
# find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums
# O(N), O(N)
from collections import Counter
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freqs = Counter(nums) # Counter({1: 2, 2: 2, 3: 1})
        degree = max(freqs.values()) # 2
        
        if degree == 1: return 1
        
        res = float('inf')
        candidates = [n for n in freqs if freqs[n] == degree] # [1, 2]
        
        for candidate in candidates:
            l = nums.index(candidate)
            r = len(nums) - nums[::-1].index(candidate) - 1
            res = min(res, r - l + 1)
            
        return res
