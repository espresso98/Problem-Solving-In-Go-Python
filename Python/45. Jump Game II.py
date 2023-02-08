# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
# Greedy: O(N),O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        jumps = 0
        while r < len(nums) - 1:
            nxt = max(i + nums[i] for i in range(l, r + 1))  # farthest position
            l, r = r + 1, nxt
            jumps += 1
        return jumps

        # l, r = 0, 0
        # jumps = 0
        # while r < len(nums) - 1:
        #     farthest = 0  
        #     for i in range(l, r + 1):
        #         farthest = max(farthest, i + nums[i])
        #     l = r + 1
        #     r = farthest
        #     jumps += 1
        # return jumps
