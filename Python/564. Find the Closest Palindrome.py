# 88 -> 77
# 121 -> 111
# 1337 -> 1331
# 2446 -> 2442
# 5000 -> 5005
# 1234 -> 1221
# 999  -> 1001
# 12932 -> 12921
# 99800 -> 99799
# 12120 -> 12121

# The closest is defined as the absolute difference minimized between two integers.
# TC: O(N), SC: O(N)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)  # n= "123", num = 123
        # processing edge cases
        # 1, ...10, and 100, 1000, 10000, ...
        if int(n) <= 10 or (n[0] == '1' and all(d == '0' for d in n[1:])): 
            return str(num - 1)
        # 99, 999, 9999, ....
        elif all(d == '9' for d in n): 
            return str(num + 2)
        # 11, 1001, 10001, ...
        elif n[0] == '1' and n[-1] == '1' and all(d == '0' for d in n[1:-1]):
            return str(num - 2)
        
        # build a palindrome with prefix and its reverse
        N = len(n)
        def build_palindrome(P):
            first = str(P)
            second = first[:-1] if N % 2 == 1 else first[:]
            return int(first + second[::-1])  # odd: '12 -> '121', even: '12 -> '1221'

        # get first half including the mid = prefix
        P = int(n[:(N+1)//2])
        # get candidates
        C = list(map(build_palindrome, (P-1, P, P+1))) # [111, 121, 131]
        # pick the candidate having min abs difference
        return str(min((c for c in C if c != num), key=lambda c: abs(num-c)))