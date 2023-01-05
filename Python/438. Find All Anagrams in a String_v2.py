# O(N) / O(1)
# Approach: Sliding Window with HashMap
from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []   
        if len(p) > len(s):
             return res

        hash_p = Counter(p)
        hash_s = defaultdict(int)

        l = 0
        for r in range(len(s)):
            hash_s[s[r]] += 1
            if r - l + 1 > len(p):
                hash_s[s[l]] -= 1
                if hash_s[s[l]] == 0: 
                    del hash_s[s[l]]
                l += 1
            if hash_s == hash_p:
                res.append(l)  
                      
        return res
        