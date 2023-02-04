# O(N), O(N)
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        diff = ord('a') - ord('A') # 32
        for ch in s:
            if stack and abs(ord(stack[-1])-ord(ch)) == diff: 
                stack.pop()                                
            else: stack.append(ch)                          
        return ''.join(stack)    
        