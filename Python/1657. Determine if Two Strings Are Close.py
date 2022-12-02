import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2) or len(word1) != len(word2): 
            return False        
        map1 = collections.Counter(word1)
        map2 = collections.Counter(word2)
        return sorted(map1.values()) == sorted(map2.values())
        