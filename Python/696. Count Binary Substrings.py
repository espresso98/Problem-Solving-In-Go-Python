# return the number of non-empty substrings that have the same number of 0's and 1's
# all the 0's and all the 1's in these substrings are grouped consecutively.
# O(N), O(N)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group_cnts = [1]             # [2, 2, 2, 2]
        for i in range(1, len(s)):   # s: "00110011"
            if s[i-1] != s[i]:
                group_cnts.append(1)
            else: 
                group_cnts[-1] += 1

        res = 0
        for i in range(1, len(group_cnts)):
            res += min(group_cnts[i-1], group_cnts[i])
        return res

# O(N), O(1)
class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        prev_gr_cnts, cur_gr_cnts = 0, 1    

        for i in range(1, len(s)):
            if s[i-1] != s[i]:   # s: "00110011"
                res += min(prev_gr_cnts, cur_gr_cnts)
                prev_gr_cnts, cur_gr_cnts = cur_gr_cnts, 1
            else: 
                cur_gr_cnts += 1            
        return res + min(prev_gr_cnts, cur_gr_cnts)
            