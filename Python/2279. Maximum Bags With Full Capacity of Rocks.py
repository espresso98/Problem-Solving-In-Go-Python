# O(nlogn), O(n)
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        vacancy = [c - r for c, r in zip(capacity, rocks)]
        vacancy.sort()  # [0, 1, 1, 1]

        full_bags = 0
        for v in vacancy:
            if additionalRocks >= v:
                additionalRocks -= v
                full_bags += 1
            else: 
                break
        return full_bags
        