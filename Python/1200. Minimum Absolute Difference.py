# find all pairs of elements with the minimum absolute difference of any two elements.
# TC: O(NlogN), SC: O(N) - python sorthing algorithm
import math

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        res = []

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < min_diff:
                min_diff = arr[i] - arr[i-1]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                res.append([arr[i-1], arr[i]])
        return res
