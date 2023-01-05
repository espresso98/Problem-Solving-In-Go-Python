# Return the length of the longest substring containing the same letter
# the length of the longest substring = window size
# O(N), O(26)
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(count.values())
            while  r - l + 1 > max_freq + k:   # window size: r-l+1, k: replacements
                count[s[l]] -= 1                 
                l += 1    # decrease window
            res = max(res, r - l + 1)
        return res
