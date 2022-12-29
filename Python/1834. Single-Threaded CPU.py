# Shortest Job First (SJF) CPU Scheduling
# O(NlogN), O(N)
from heapq import heappush, heappop
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((*task, i) for i, task in enumerate(tasks))
        # tasks: [(1, 2, 0), (2, 4, 1), (3, 2, 2), (4, 1, 3)]
        order, min_heap = [],[]
        i, cur_time = 0, tasks[0][0]

        while min_heap or i < len(tasks):
            # Push all the tasks whose enqueueTime <= currtTime into the heap.
            while i < len(tasks) and tasks[i][0] <= cur_time:
                heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            # cur_time, min_heap: 1 [[2, 0]] 3 [[2, 2], [4, 1]] 5 [[1, 3], [4, 1]] 6 [[4, 1]]
            # When the heap is empty, try updating cur_time to next task's enqueue time.
            if not min_heap:
                cur_time = tasks[i][0]   
            else: # Complete this task and increment cur_time.
                proc_time, idx = heappop(min_heap)
                cur_time += proc_time
                order.append(idx)
        return order
