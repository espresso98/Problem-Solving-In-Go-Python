# O(logP), O(1)
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p, q = p // 2, q // 2

        if p % 2 == 1 and q % 2 == 0:    # p:odd, q: even 3, 2
            return 0
        elif p % 2 == 1 and q % 2 == 1:  # p:odd, q: odd  1, 1
            return 1
        elif p % 2 == 0 and q % 2 == 1:  # p:even, q: odd 2, 1
            return 2
            