# TC: O(n), SC: O(1)
def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 1: return n
    
    k = 1
    for i in range(1, n):
        if nums[i-1] < nums[i]:
            nums[k] = nums[i]
            k += 1
    return k
    