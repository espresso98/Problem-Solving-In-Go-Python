# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
# 1 <= k <= num.length <= 105
# O(N), O(N)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): 
            return "0"

        st = []
        for digit in num:
            while k > 0 and st and st[-1] > digit:
                st.pop()
                k -= 1
            if st or digit != '0':
                st.append(digit)

        while k > 0 and st:
            st.pop()
            k -= 1
      
        return ''.join(st) if st else '0'
