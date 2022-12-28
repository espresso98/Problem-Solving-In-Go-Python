# Greedy + Max Heap, O(N + klogN), O(N)
# An array can be converted to a heap in linear time (O(n)) using a method like Python's heapq.heapify()

# There are two ways to create a heap of n elements:
# heapify an existing array of n elements: O(n) of time complexity;
# create an empty heap instance, and then enqueue n elements one by one: O(nlogn)of time complexity.

from heapq import heapify, heapreplace
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]  
        heapify(heap)         
        for _ in range(k):
            heapreplace(heap, heap[0] // 2)
        return -sum(heap)    


"""
https://docs.python.org/3/library/heapq.html

heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.

heapq.heapreplace(heap, item)
Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.
"""
