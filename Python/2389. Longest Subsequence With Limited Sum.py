# O(nlogn+mlogn) = O((m+n)⋅log⁡n), O(n)
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()                     # [1, 2, 4, 5]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]        # [1, 3, 7, 12]
        res = [self.binary_search(nums, q) for q in queries]
        return res

    def binary_search(self, nums, target):
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2   # q: [3, 10, 21] 
            if nums[mid] <= target:  # n: [1, 3, 7, 12]]
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res + 1     


import bisect
class Solution2:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()                     
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]        
        res = []
        for query in queries:
            idx = bisect.bisect_right(nums, query)
            res.append(idx)
        return res

# bisect(list, num, beg, end) 
# : This function returns the position in the sorted list, where the number passed in argument can be placed 
#   so as to maintain the resultant list in sorted order. If the element is already present in the list, 
#   the rightmost position where element has to be inserted is returned.