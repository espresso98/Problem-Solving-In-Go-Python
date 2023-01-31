# 1 <= haystack.length, needle.length <= 104
# O(N), O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        # if n == 0: return 0
        if n > h: return -1
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
        