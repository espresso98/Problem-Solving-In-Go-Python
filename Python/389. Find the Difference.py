class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Solution1
        for i in t:
            if s.count(i) != t.count(i):
                return i
            
        # Solution2. Hashmap: O(N), O(1)
        cnt_s = Counter(s)
        for ch in t:
            if ch not in cnt_s:
                return ch
            else:
                cnt_s[ch] -= 1
                if cnt_s[ch] == 0:
                    cnt_s.pop(ch)
        # Solution3
        for i in t:
            if i not in s or s.count(i) < t.count(i):
                return i
                