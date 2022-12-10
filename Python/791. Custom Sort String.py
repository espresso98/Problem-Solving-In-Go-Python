# Permute the characters of s so that they match the order that order was sorted. More specifically, 
# if a character x occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.

# TC: O(len(order) + len(s)), SC: O(len(s))
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_cnt = collections.Counter(s)
        res = []

        for ch in order:
            if ch in s: 
                res.append(ch * s_cnt[ch])
                s_cnt.pop(ch)

        for ch in s_cnt:
            res.append(ch * s_cnt[ch])

        return ''.join(res)
