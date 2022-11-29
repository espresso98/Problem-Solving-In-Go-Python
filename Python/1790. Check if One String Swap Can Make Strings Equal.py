class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2): 
            return False
            
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        if not diff: 
            return True
        if len(diff) == 2: 
            return diff[0][::-1] == diff[1]
        return False
        