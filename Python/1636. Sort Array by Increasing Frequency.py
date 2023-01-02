from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        return sorted(nums, key=lambda x: [freqs[x], -x])
