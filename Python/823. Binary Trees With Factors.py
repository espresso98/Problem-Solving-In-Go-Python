# Each non-leaf node's value should be equal to the product of the values of its children.
# O(n^2) / O(n)
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()  # [2,4,5,10]
        MOD = 10**9 + 7
        dp = Counter()
        for a in arr: 
            cnt = 1
            for b in arr: 
                if b > a: break
                if a % b == 0:
                    cnt += dp[b] * dp[a//b]   # dp[6] += dp[2] * dp[3]
            dp[a] = cnt
        # Counter({10: 3, 4: 2, 2: 1, 5: 1})
        return sum(dp.values()) % MOD

class Solution2:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        for a in sorted(arr):
            dp[a] = 1 + sum(dp[b] * dp.get(a//b,0) for b in dp if a % b == 0)
        return sum(dp.values()) % (10**9 + 7)
