# On each turn, we choose the heaviest two stones and smash them together. 
# O(NlogN), O(N)

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-val for val in stones]
        heapq.heapify(min_heap)  # [-8,-7,-4,-1,-2,-1] [-4,-2,-1,-1,-1]

        while len(min_heap) > 1:
            stone1 = heapq.heappop(min_heap)
            stone2 = heapq.heappop(min_heap)
            diff = stone1-stone2
            heapq.heappush(min_heap, diff)
            
        return -min_heap[0] if min_heap else 0  # [-1]
