# Prefix Sums and Counting: O(N), O(K)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = rsum = 0
        remainders = {0:1}    
        
        for num in nums:  
            rsum += num  
            remain = rsum % k
            if remain in remainders:
                res += remainders[remain]
                remainders[remain] += 1
            else: 
                remainders[remain] = 1
        return res

# O(N), O(K)  Prefix sum + Hashmap  
# sum(i, j) = sum(0, j) - sum(0, i) 
# if sum(0, i) % K == sum(0, j) % K, sum(i, j) is divisible by K 
import collections
class Solution2:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:       
        res = prefix_sum = 0
        remainders = collections.defaultdict(int)
        remainders[0] = 1

        for num in nums:
            prefix_sum += num
            rem  = prefix_sum % k
            if rem in remainders:       
                res += remainders[rem]  
            remainders[rem] += 1
        return res 
