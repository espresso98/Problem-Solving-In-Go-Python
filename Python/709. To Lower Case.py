# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
# ord/chr: convert a character to an int and vice versa.
# s.lower()
# O(N), O(1)
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        diff = ord('a') - ord('A')
        for ch in s:
            if ord('A') <= ord(ch) <= ord('Z'):
                res += chr(ord(ch) + diff)
            else: 
                res += ch
        return res
