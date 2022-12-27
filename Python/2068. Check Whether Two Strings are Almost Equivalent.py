# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3
from collections import Counter
# Solution1
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        diff_cnts = Counter(word1) 
        for w in word2:  
            diff_cnts[w] -= 1
        diff_freq = map(abs, diff_cnts.values())
        return all(diff <= 3 for diff in diff_freq) 

# Solution2
class Solution2:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:        
        diff_cnts = [0] * 26
        for ch in word1:
            diff_cnts[ord(ch) - ord('a')] += 1
        for ch in word2:
            diff_cnts[ord(ch) - ord('a')] -= 1
        for i in range(26):
            if abs(diff_cnts[i]) > 3:
                return False
        return True

# Solution3
 class Solution3:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1, w2 = Counter(word1), Counter(word2)
        for ch in set(list(w1.keys()) + list(w2.keys())):
            if abs(w1[ch] - w2[ch]) > 3:
                return False
        return True
