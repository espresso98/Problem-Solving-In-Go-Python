class Solution:
    # Solution1: O(N), O(N)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        num_set = set(nums)
        for n in range(1, len(nums)+1):
            if n not in num_set:
                res.append(n)
        return res

class Solution2:
    # idx          0  1  2  3  4  5  6  7 
    # new_idx      3  2  1  6  7  1  2  0      new_idx = nums[i] - 1
    # nums[i]     -4 -3 -2 -7  8  2  3 -1  

    # Solution2: O(N), O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            new_idx = abs(num) - 1   # val -> idx 
            nums[new_idx] = -abs(nums[new_idx])      # negative mark
        return [i + 1 for i, num in enumerate(nums) if num > 0]  # idx -> val

