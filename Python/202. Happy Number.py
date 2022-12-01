# Detect Cycles with a HashSet
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(d)**2 for d in str(n)])
            if n == 1:
                return True
        return False

        # def SquareOfNumbers(a):
        #     Sum = 0
        #     while a > 0:
        #         digit = a%10
        #         Sum+=(digit*digit)
        #         a = a//10
        #     return Sum
        