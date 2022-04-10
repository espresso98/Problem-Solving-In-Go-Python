# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = [ch.lower() for ch in s if ch.isalnum()]
        left, right = 0, len(alnum) - 1
        while left < right:
            if (alnum[left] != alnum[right]):
                return False
            left += 1
            right -= 1
        return True
        
                    
# TC: O(n), SC: O(1)