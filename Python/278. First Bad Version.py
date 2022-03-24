# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Approach: Binary Search
# TC: O(logn), SC: O(1)
# Approach: Binary Search
# TC: O(logn), SC: O(1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high-low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid+1
        return low
        

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.        