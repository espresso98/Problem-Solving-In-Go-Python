# O(N), O(N)
class Solution:
    def nextPalindrome(self, num: str) -> str:
        N = len(num)
        mid = N // 2
        midStr = num[mid] if N % 2 else ""
        leftHalf = self.nextGreater(num[:mid])
        return leftHalf + midStr + leftHalf[::-1] if leftHalf else ""
    
    # find the next permutation that is greater than the first half of the palindrome
    def nextGreater(self, s):
        N = len(s)
        s = list(s) 
        # find longest decreasing suffix
        i = N - 2
        while i >= 0 and s[i] >= s[i+1]:
            i -= 1  
        if i < 0: return ""
        # find rightmost successor in the suffix
        j = N - 1
        while j >= 0 and s[i] >= s[j]:
            j -= 1
        # swap pivot and successor
        s[i], s[j] = s[j], s[i]
        # reverse the suffix
        l, r = i + 1, N - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
