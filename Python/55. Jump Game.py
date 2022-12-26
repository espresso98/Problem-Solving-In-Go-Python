# Greedy approach: O(N), O(1)
# We call a position in the array a "good index" if starting at that position, we can reach the last index.
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIdx = len(nums) - 1              # i: [0,1,2,3,4] [0,1,2,3,4]
        for i in range(len(nums) - 1, -1, -1):   # n: [2,3,1,1,4] [2,3,1,1,4]
            if i + nums[i] >= lastGoodIdx:
                lastGoodIdx = i    # can reach at ith position to the i+1th index
        return lastGoodIdx == 0

# O(N), O(1)
class Solution2:
    def canJump(self, nums: List[int]) -> bool:    
        max_reach_idx = 0
        for idx, jump in enumerate(nums):  # i: [0,1,2,3,4]
            if max_reach_idx < idx:        # n: [2,3,1,1,4]
                return False
            if max_reach_idx >= len(nums) - 1:
                return True
            max_reach_idx = max(max_reach_idx, idx + jump)
            # print(f"idx = {idx}, jump={jump}, max_reach_idx={max_reach_idx}")
            # idx = 0, jump=2, max_reach_idx=2
            # idx = 1, jump=3, max_reach_idx=4
