# O(N), O(N)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        D = list(str(n))
        N = len(D)
        # find first decreasing element starting from backward
        i = N - 2
        while i >= 0 and D[i] >= D[i+1]:
            i -= 1  
        if i < 0: return -1
        # find number just larger than it then swap them
        j = N - 1
        while j >= 0 and D[i] >= D[j]:
            j -= 1
        D[i], D[j] = D[j], D[i]
        # reverse the suffix
        l, r = i + 1, N - 1
        while l < r:
            D[l], D[r] = D[r], D[l]
            l += 1
            r -= 1
        res = int(''.join(D))
        return res if res < 1<<31 else -1