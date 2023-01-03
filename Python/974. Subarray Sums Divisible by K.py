# Prefix Sums and Counting: O(N+K), O(K)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = rsum = 0
        prefix = {0:1}    
        
        for num in nums:  
            rsum += num  
            remain = rsum % k
            if remain in prefix:
                res += prefix[remain]
                prefix[remain] += 1
            else: 
                prefix[remain] = 1
        return res
        