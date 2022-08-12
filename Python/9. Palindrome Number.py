# O(log 10(n)), O(1)
# Approach: Revert half of the number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): 
            return False
        
        reverse = 0
        temp = x
        while temp > 0:
            reverse = reverse * 10 + temp % 10
            temp //= 10
        return x == reverse


# Input: x = 121
# Output: true