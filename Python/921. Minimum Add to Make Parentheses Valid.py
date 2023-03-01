# O(N), O(N)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for p in s:
            if p == "(":
                stack.append(p)
            elif p == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
        return len(stack)
            

# O(N), O(1)
class Solution2:
    def minAddToMakeValid(self, S):
        open = close = 0
        for p in S:
            if p == '(':
                open += 1
            elif p == ')':
                if open > 0:
                    open -= 1
                else:
                    close += 1
        return open + close
