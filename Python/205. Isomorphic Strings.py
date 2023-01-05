# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# O(N), O(26*2)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}

        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = t[i] 
            elif s_map[s[i]] != t[i]:
                return False
            if t[i] not in t_map: 
                t_map[t[i]] = s[i]
            elif t_map[t[i]] != s[i]:
                return False
        return True
            