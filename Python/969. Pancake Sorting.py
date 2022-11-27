# TC: O(N^2), SC: O(N)
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        i = 0
        for x in range(len(arr), 1, -1):
            max_idx = arr.index(x)
            res.extend([max_idx+1, x])
            arr = arr[:max_idx+1][::-1] + arr[max_idx+1:]
            arr = arr[x-1::-1] + arr[x:]
        return res
        