class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = [0] * 26
        s2_map = [0] * 26
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1 # a, b
            s2_map[ord(s2[i]) - ord('a')] += 1 # e, i
        
        for i in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True
            s2_map[ord(s2[i-len(s1)]) - ord('a')] -= 1 # remove e
            s2_map[ord(s2[i]) - ord('a')] += 1 # add d
            
        return s1_map == s2_map
        