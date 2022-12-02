# O(N^2), O(1)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        # subarr = []
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                # subarr.append(arr[i:j+1])
                res += sum(arr[i:j+1])
        return res

# O(N), O(1)  
class Solution2:                        
    def sumOddLengthSubarrays(self, arr):
        res, n = 0, len(arr)
        for i, a in enumerate(arr):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res
        