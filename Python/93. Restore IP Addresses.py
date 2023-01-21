# valid : exactly four integers separated by single dots
# each integer : between 0 and 255
#              : cannot have leading zeros.
# Approach: Backtracking (DFS)
# TC: O(M^N*N) where O(M^N−1) possibilities * O(M⋅N) valid check, here M=3, N=4
# SC: O(M*N)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        N = len(s)

        if N < 4 or N > 12:
            return res
        
        def backtrack(i, dots, current):
            if dots < 0: 
                return

            if i == N:
                if dots == 0:
                    res.append(".".join(current))
                return
             
            if s[i] == "0":
                current.append("0")
                backtrack(i+1, dots-1, current)
                current.pop()
                return
            
            for j in range(3):
                if i + j < N and  0 <= int(s[i:i+j+1]) <= 255:
                    current.append(s[i:i+j+1])
                    backtrack(i+j+1, dots-1, current)
                    current.pop()
                    
        backtrack(0, 4, [])
        return res
        

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
