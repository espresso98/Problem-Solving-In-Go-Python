# TC: O(N), SC: O(N)
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0  # max_length
        max_q = deque()
        min_q = deque()
       
        l = 0
        for r, n in enumerate(nums):
            while max_q and n > max_q[-1]:
                max_q.pop()
            max_q.append(n)

            while min_q and n < min_q[-1]:
                min_q.pop()
            min_q.append(n)

            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft()
                l += 1
                      
            res = max(res, r-l+1)

        return res