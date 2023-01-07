# O(N), O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1, step2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            step3 = cost[i] + min(step1, step2)
            step1, step2 = step2, step3
        return min(step1, step2)
