# Calculate diff = (sum(A) - sum(B)) / 2
# We want find a pair (a, b) with a = b + diff
# O(M+N), O(N)

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A, B = aliceSizes, bobSizes 
        diff = (sum(A) - sum(B)) // 2
        A = set(A)
        
        for b in set(B):
            if b + diff in A:
                return [b + diff, b]

# Input: aliceSizes = [1,2,5], bobSizes = [2,4]
# Output: [5,4]