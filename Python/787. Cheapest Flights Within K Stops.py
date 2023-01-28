import collections
import heapq
from typing import List

# Solution1: Dijkstra. O(V+E⋅K⋅log(E⋅K)) where E be the number of flights and V be the number of cities
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)    # O(E)
        for u, v, w in flights:
            graph[u].append((v, w))  # {0: (1, 100), 1: (3, 600), 2: (3, 200)}

        pq = [(0, src, k + 1)]
        visited = [0] * n      # T, S: O(V)
        while pq:              # [(0, 0, 2)]  [(100, 1, 1)]  [(200, 2, 0), (700, 3, 0)]
            cost, node, stops = heapq.heappop(pq)
            if node == dst:
                return cost
            if visited[node] >= stops: 
                continue
            visited[node] = stops
            for v, w in graph[node]:
                heapq.heappush(pq, (cost + w, v, stops - 1))
        return -1

# Solution2: BFS. O(V+E*K), O(V+E*K) where E be the number of flights and V be the number of cities
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj  = [[] for _ in range(n)]  
        cost = [float('inf') for _ in range(n)] # O(V)
        cost[src] = 0
        for u, v, w in flights:
            adj[u].append((v,w))
        # [[(1, 100)], [(2, 100), (3, 600)], [(0, 100), (3, 200)], []]
        q = collections.deque([(src,-1,0)])   # T, S: O(E*K)
        while q:
            u, stops, cost = q.popleft()
            if u == dst and stops <= k: 
                return cost[dst]
            for v, w in adj[u]:
                if cost[v] > cost + w:
                    cost[v] = cost + w
                    q.append((v, stops+1, cost+w))
            # deque([(1, 0, 100)])  deque([(2, 1, 200), (3, 1, 700)])
            # [0, 100, inf, inf]  [0, 100, 200, 700]
        return cost[dst] if cost[dst] != float('inf') else -1
