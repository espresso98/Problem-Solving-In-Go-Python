# n one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x
# O(N), O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x
        if target < 0: return -1
        elif target == 0: return n

        max_subarr_len = -1
        prefix_sum = 0
        l = 0 
        for r in range(n):     # [1,1,4,2,3] target = 11-5 = 6
            prefix_sum += nums[r]      # [1,2,6,8,11]
            while prefix_sum > target and l <= r:
                prefix_sum -= nums[l]  # shrink sliding window
                l += 1
            if prefix_sum == target:
                max_subarr_len = max(max_subarr_len, r-l+1)
                print(max_subarr_len)
        return n - max_subarr_len if max_subarr_len != -1 else -1
