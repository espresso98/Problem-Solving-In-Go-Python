# O(s+t), O(s+t)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(s:str) -> str:
            stack = []
            for ch in s:
                if ch == '#':
                    if stack: stack.pop()
                else:
                    stack.append(ch)  
            return ''.join(stack)  

        return build_string(s) == build_string(t)
        