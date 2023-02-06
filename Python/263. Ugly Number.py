# O(log⁡(N)), O(1)
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:  # A non-positive integer cannot be ugly
            return False
        # if n == 1:
        #     return True
        factors = [2,3,5]
        for f in factors:
            # Keep dividing dividend by divisor when division is possible
            while n % f == 0: 
                n //= f
        return n == 1 

# 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.