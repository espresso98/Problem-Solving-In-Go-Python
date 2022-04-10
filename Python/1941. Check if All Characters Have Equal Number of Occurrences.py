# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
# return true if length of set is one (all characters Have same number of occurrences)
# TC: O(n), SC: O(1)

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        return len(set(d.values())) == 1

#     def areOccurrencesEqual(self, s: str) -> bool:
#         d = defaultdict(int)
#         for k in s:
#             d[k] += 1

#         res = set()        
#         for i in d.values():
#             res.add(i)
#         return len(res) == 1


#     def areOccurrencesEqual(self, s: str) -> bool: 
#         return len(set(Counter(s).values())) == 1