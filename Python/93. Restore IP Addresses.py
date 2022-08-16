# valid : exactly four integers separated by single dots
# each integer : between 0 and 255
#              : cannot have leading zeros.
# decision tree. 3 decisions. 3^12. len <= 12
# Approach: Backtracking (DFS)

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        
        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return 
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (len(s[i:j+1]) == 1 or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curIP + s[i:j+1] + "." )
                     
        backtrack(0, 0, "")
        return res
    
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]