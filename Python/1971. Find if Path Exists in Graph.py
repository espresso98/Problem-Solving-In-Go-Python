# adjacency_graph = {0: [1, 2], 1: [0, 2], 2: [1, 0]})
# BFS, O(V+E), O(V+E)
from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1 or [source, destination] in edges or [destination, source] in edges:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        if source not in graph or destination not in graph:
            return False

        q = deque([source])
        seen = set()
        while q:
            cur_node = q.popleft()
            if cur_node == destination:
                return True 
            seen.add(cur_node)
            for next_node in graph[cur_node]:
                if next_node not in seen:
                    q.append(next_node)    
        return False

if __name__  == '__main__':
    s = Solution()
    print(s.validPath(n=3, edges=[[0,1],[1,2],[2,0]], source=0, destination=2))
    print(s.validPath(n=6, edges=[[0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))

"""
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
"""