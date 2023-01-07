# O(N), O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1

        cur_tank, start = 0, 0
        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]  # diff
            if cur_tank < 0:
                start = i + 1
                cur_tank = 0
        return start 
