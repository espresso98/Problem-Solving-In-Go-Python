# TC:O(N), SC:O(N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []      
        for n in nums2:
            while stack and stack[-1] < n:
                greater[stack.pop()] = n
            stack.append(n)

        res = []
        for n in nums1:
            if n in greater:
                res.append(greater[n])
            else:
                res.append(-1)
        return res
