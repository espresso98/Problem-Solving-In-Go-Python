# O(N), O(N)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
           

# Input: s = "azxxzy"
# Output: "ay"