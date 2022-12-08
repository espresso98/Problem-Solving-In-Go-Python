# One Hash Map. O(N), 0(26) -> 0(1)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): 
            return False

        mag_cnt = Counter(magazine)
        for ch in ransomNote:
            if ch not in mag_cnt or mag_cnt[ch] <= 0:
                return False
            else: 
                mag_cnt [ch] -= 1          
        return True


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote))
