# Prefix Sum: O(N), O(1)
import math
from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        idx, n, total = -1, len(nums), sum(nums)
        min_avg_diff = math.inf
        pref_sum = 0
        
        for i in range(n):
            pref_sum += nums[i]
            suff_sum = total - pref_sum
            suff_avg = suff_sum // (n - i - 1) if i != n - 1 else 0
            cur_diff = abs(pref_sum // (i + 1) - suff_avg)
            if cur_diff < min_avg_diff:
                min_avg_diff = cur_diff
                idx = i
        return idx
