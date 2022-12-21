# We want to split a group of n people (labeled from 1 to n) into two groups of any size.
# O(V+E), O(V+E) where V is the number of people and E is the size of dislikes
from collections import deque
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(node):
            q = deque([node])
            color[node] = 0  # red
            while q:
                a = q.popleft()
                for b in graph[a]:
                    if color[b] == color[a]: # conflict
                        return False
                    if color[b] == -1:
                        color[b] = 1 - color[a]   # 0: red, 1: blue
                        q.append(b)
            return True

        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        # [[], [2, 3], [1, 4], [1], [2]]
        color = [-1] * (n + 1)   # 0: red, 1: blue
        # [-1, 0, 1, 1, 0]
        for a in range(1, n + 1):
            if color[a] == -1:
                if not bfs(a):
                    return False
        return True

# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4] and group2 [2,3]
