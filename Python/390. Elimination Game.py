# O(logN), O(1)
class Solution:
    def lastRemaining(self, n: int) -> int:
        isLeft = True
        start = jump = 1
        while n > 1:
            if isLeft or n % 2:  # odd remaining
                start += jump    # next start after elimination
            n //= 2              # O(logN)
            jump *= 2
            isLeft = not isLeft  # isLeft ^= True
        return start
