# O(M+N), O(1)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m-n) > 1: 
            return False
        
        diff_cnt = 0
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if diff_cnt == 1:
                    return False
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1
                diff_cnt += 1
            
        if i < m or j < n:
            diff_cnt += 1   
            
        return diff_cnt == 1
            
# Input: s = "ab", t = "acb"
# Output: true