# TC: O(1), SC: O(1)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Soultion 1
        range = high + 1 - low
        if low % 2 == 1 and high % 2 == 1:
            return range // 2 + 1
        else:
            return range // 2

        # Solution 2
        return (high + 1) // 2 - low // 2   
        