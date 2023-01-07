# A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two. 
# 0 <= deliciousness[i] <= 220
# O(22*N), O(N)
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = [2**i for i in range(22)]   
        print(powers)
        seen = collections.defaultdict(int)  
        res = 0
        MOD = 10**9 + 7

        for score in deliciousness:          # [1,1,1,3,3,3,7]
            for pow in powers:               # [1, 2, 4, 8, 16, 32, 64, 128, ... , 1048576, 2097152]
                if pow - score in seen:      # {}, {1: 1}, {1: 2}, ..., {1: 3, 3: 3, 7: 1})
                    res += seen[pow - score] # (1,1): 3 ways, (1,3):9 ways, (1,7): 3 ways
            seen[score] += 1
        return res % MOD
