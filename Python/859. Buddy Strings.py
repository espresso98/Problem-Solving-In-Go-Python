# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
# O(N), O(1) if len(diff) > 2, it will return False, so space is O(1).
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) != len(goal): 
            return True
        diff = []
        for a, b in zip(s, goal): 
            if a != b:
                diff.append((a,b))
            if len(diff) > 2:
                return False
        return len(diff) == 2 and diff[0] == diff[1][::-1]
