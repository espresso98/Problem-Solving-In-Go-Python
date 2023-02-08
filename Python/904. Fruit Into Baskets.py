# contiguous subarray which have 2 distinct type
# Sliding window: O(N), O(N)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        type_cnts = collections.defaultdict(int)  # {type: cnt}
        l = 0
        for r, fruit in enumerate(fruits):
            type_cnts[fruit] += 1
            if len(type_cnts) > 2:
                type_cnts[fruits[l]] -= 1
                if type_cnts[fruits[l]] == 0:
                    del type_cnts[fruits[l]]
                l += 1
        return r - l + 1  # logest contiguous subarry size, window 
