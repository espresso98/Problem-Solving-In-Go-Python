# O(Nlogk), O(N+k) where N, k is elements for Counter and heap respectively.
from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnts = Counter(nums)  # {1: 3, 2: 2, 3: 1}
        heap = [(-freq, num) for num, freq in num_cnts.items()]
        heapify(heap)  # [(-3, 1), (-2, 2), (-1, 3)]
        return [heappop(heap)[1] for _ in range(k)]
