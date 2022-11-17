# Check if all the numbers in s are strictly increasing from left to right 
class Solution:
    # Solution 1. TC: O(nlogn), SC: O(n)
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        for w in s.split():
            if w.isdigit():
                nums.append(int(w))
        return len(set(nums)) == len(nums) and nums == sorted(nums)
 
    # Solution 2. TC: O(n), SC: O(n)
        nums = [int(w) for w in s.split() if w.isdigit()]

        for i in range(len(nums) - 1):
            if nums[i + 1] <= nums[i]:
                return False
        return True
        
    # Solution 3. TC: O(n), SC: O(n)
        nums = [int(w) for w in s.split() if w.isdigit()]
        return all(nums[i-1] < nums[i] for i in range(1, len(nums)))
        
                