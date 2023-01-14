# O(Nlogk), O(N+k) where N, k is elements for Counter and heap respectively.
from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnts = Counter(nums)  # {1: 3, 2: 2, 3: 1}
        heap = [(-freq, num) for num, freq in num_cnts.items()]
        heapify(heap)  # [(-3, 1), (-2, 2), (-1, 3)]
        return [heappop(heap)[1] for _ in range(k)]


# Bucket sort: O(N), O(N)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = collections.Counter(nums)      # {1: 3, 2: 2, 3: 1}
        freqs = [[] for i in range(len(nums) + 1)]
        
        for num, cnt in count_nums.items():       # freq    0    1    2    3    4   5   6 
            freqs[cnt].append(num)                # bucket [[], [3], [2], [1], [], [], []]

        res = []
        for freq in range(len(freqs) - 1, 0, -1 ):
            for n in freqs[freq]:
                res.append(n)
                if len(res) == k:
                    return res
            