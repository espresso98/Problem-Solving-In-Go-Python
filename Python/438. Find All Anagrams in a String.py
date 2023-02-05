# O(N) / O(1)
# Approach: Sliding Window with HashMap
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []   
        window_size = len(p)
        hash_p = defaultdict(int)
        hash_s = defaultdict(int)
        
        if len(p) > len(s):
             return res
            
        for ch in p:
            hash_p[ch] += 1
            
        for i in range(len(s)):
            # add one more letter on the right side
            hash_s[s[i]] += 1
            # remove one letter from the left side
            if i >= window_size:
                if hash_s[s[i-window_size]] == 1:
                    del hash_s[s[i-window_size]]
                else: 
                    hash_s[s[i-window_size]] -= 1
            # compare hashmap s in the window with hashmap p
            if hash_s == hash_p:
                res.append(i-window_size+1)    
        return res

"""
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


# O(N) / O(1)
# Approach: Sliding Window with HashMap
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
             return []
        
        p_cnt, s_cnt = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            p_cnt[p[i]] += 1 
            s_cnt[s[i]] += 1

        res = [0] if s_cnt == p_cnt else []  
        l = 0
        for r in range(len(p), len(s)):
            s_cnt[s[r]] += 1
            s_cnt[s[l]] -= 1
            if s_cnt[s[l]] == 0:
                s_cnt.pop(s[l])
            l += 1
            if s_cnt == p_cnt:
                res.append(l)
            
        return res
