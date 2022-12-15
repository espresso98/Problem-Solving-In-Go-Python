# O(N), O(1)
 def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2: return ''
        for i in range(n//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'
        