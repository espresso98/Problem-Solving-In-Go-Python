# O(Nlogk), O(n)
import heapq
import collections
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words) # {'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1}
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        # [(-2, 'i'), (-2, 'love'), (-1, 'leetcode'), (-1, 'coding')]
        # print(f"count = {count}, heap={heap}")
        return [heapq.heappop(heap)[1] for _ in range(k)]
        