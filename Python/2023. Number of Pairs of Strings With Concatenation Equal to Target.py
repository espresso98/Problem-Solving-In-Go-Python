# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # Brute Force 
        # cnt = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         cnt = cnt + (nums[i] + nums[j] == target) + (nums[j] + nums[i] == target)
        # return cnt
        
        freq = Counter(nums)
        res = 0
        # print(freq)
        # freq = defaultdic(int)
        # for num in nums:
        #     freq[str(num)] += 1
        for k, v in freq.items():
            if target.startswith(k):
                suffix = target[len(k):]
                print(suffix)
                if k == suffix:
                    res += v * (v-1)  # P(n,2)
                else: 
                    res += v * freq[suffix]       
        return res

""" 
Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
"""